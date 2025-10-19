# 🔍 금속판 문자열 OCR 최종 보고서 (OpenCV + EasyOCR 하이브리드)

본 문서는 이미지 내의 특정 금속판(금색) 영역을 정확하게 탐지하고, 해당 영역에 새겨진 5글자 형식의 문자열(영문+숫자)을 높은 정확도로 추출하기 위한 최종 솔루션의 구현 방법과 기술적 배경을 정리합니다.

---

## 1. 개요 및 기술 선택 배경

### 1.1. 최종 목표
단일 이미지 파일(`image.jpeg`) 내에 반복되는 금색 금속판 영역에서 텍스트를 추출하고, 그 결과를 CSV 파일로 저장합니다.

### 1.2. 개별 방법론 비교 및 하이브리드 선택 이유

최종 코드는 초기 시도했던 **OpenCV + Tesseract 방식**과 **EasyOCR 단독 방식**의 장점만을 결합한 것입니다.  
아래 표는 각 방법론의 특성과 한계를 비교한 것입니다.

| 구분 | 초기 시도: OpenCV + Tesseract | 단독 시도: EasyOCR | 최종 선택: 하이브리드 (OpenCV + EasyOCR) |
|:--|:--|:--|:--|
| **탐지 과정** | 금색 마스크 → 윤곽선(Contour)을 이용한 전체 영역 탐지 | 딥러닝 모델이 텍스트 주변 영역을 자동 탐지 | 금색 마스크 → 윤곽선(Contour)을 이용한 전체 영역 탐지 |
| **인식 과정** | 이미지 전처리(이진화/샤프닝) 후 Tesseract 엔진 실행 | 딥러닝 모델이 전처리 없이 텍스트 인식 | 크롭된 Sub-ROI를 EasyOCR 모델에 전달하여 인식 |
| **인식 정확도** | 낮음 (빛 반사에 취약) | 높음 (복잡한 이미지 환경 변화에 강함) | 매우 높음 (불필요한 배경 노이즈 제거 후 인식) |
| **영역 커버리지** | 높음 (금색 판 영역을 빠짐없이 탐지) | 낮음 (금속판 일부만 탐지하거나 누락) | 매우 높음 (OpenCV가 모든 금색판 탐지 보장) |
| **주요 한계점** | 인식률 낮음 | 탐지 영역 부족 | - |

### 1.3. 하이브리드 접근법 선택 이유

> **결론:** 금속판 이미지의 특성상 **“어디에 텍스트가 있다”**는 정보를 놓치면 안 됩니다.

- **OpenCV** → 금색을 기반으로 “어디”를 확실하게 탐지하는 역할 (탐지 레이어)
- **EasyOCR** → 탐지된 영역 안에서 “무슨 텍스트가 있다”를 인식 (인식 레이어)

✅ 안정적인 영역 탐지(OpenCV) + 최고 수준의 인식 정확도(EasyOCR)  
→ **OCR 효율 극대화**

---

## 2. 환경 설정 및 라이브러리 설치

### 2.1. 필수 라이브러리 목록

| 라이브러리 | 용도 |
|:--|:--|
| **easyocr** | 딥러닝 기반 문자열 인식 (OCR 엔진) |
| **opencv-python-headless** | 이미지 처리 및 금색 영역 탐지 |
| **numpy** | OpenCV 이미지 데이터 처리 |
| **csv, re** | 결과 저장 및 문자열 정규식 처리 (Python 기본 모듈) |

### 2.2. 설치 명령어

```bash
pip install easyocr opencv-python-headless numpy
```

---

## 3. 최종 코드 및 상세 설명

### 3.1. 코드 (`easyocr_solution.py`)

```python
import easyocr
import csv
import cv2
import re
import numpy as np

IMAGE_FILENAME = "image.jpeg" 

try:
    print("EasyOCR 모델 로딩 중...")
    reader = easyocr.Reader(['en'])
    print("모델 로딩 완료.")

    img = cv2.imread(IMAGE_FILENAME)
    if img is None:
        raise FileNotFoundError(f"'{IMAGE_FILENAME}' 파일을 찾을 수 없습니다.")

    TARGET_PATTERN = re.compile(r'^[A-Z0-9]{5}$')
    
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower_gold = (10, 50, 50)
    upper_gold = (35, 255, 255)
    mask = cv2.inRange(hsv, lower_gold, upper_gold)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    plates = []
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        aspect_ratio = w / float(h)
        if 0.8 < aspect_ratio < 1.3 and 50 < w < 200:
            crop_y_start = int(y + h * 0.6)
            crop_h = int(h * 0.4)
            crop_x_start = int(x + w * 0.15)
            crop_w = int(w * 0.7)
            plates.append({'x': crop_x_start, 'y': crop_y_start, 'w': crop_w, 'h': crop_h})
            
    detected_data = []
    for plate in plates:
        x, y, w, h = plate['x'], plate['y'], plate['w'], plate['h']
        roi_img = img[y:y + h, x:x + w]
        if roi_img.size == 0: continue
        results = reader.readtext(roi_img, detail=0) 
        final_text = ""
        if results:
            for text in results:
                clean_text = text.strip().replace('\n', '').replace(' ', '').upper()
                if TARGET_PATTERN.match(clean_text):
                    final_text = clean_text
                    break
                if not final_text and 4 <= len(clean_text) <= 6:
                    final_text = clean_text
        if final_text:
            detected_data.append((x, y, w, h, final_text))
            print(f"Detected: {final_text} at ({x}, {y})")

    CSV_FILENAME = 'results_hybrid_easyocr.csv'
    with open(CSV_FILENAME, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['filename', 'x', 'y', 'w', 'h', 'text'])
        for x, y, w, h, text in detected_data:
            writer.writerow([IMAGE_FILENAME, x, y, w, h, text])
             
    print(f"✅ 완료: {len(detected_data)}개 감지됨, {CSV_FILENAME}에 저장.")

except FileNotFoundError as e:
    print(f"오류: {e}")
except Exception as e:
    print(f"실행 오류: {e}")
```

---

## 4. 실행 방법

1. 위 코드를 `easyocr_solution.py` 파일로 저장합니다.  
2. 분석할 이미지 파일(`image.jpeg`)을 같은 폴더에 둡니다.  
3. 터미널에서 다음 명령어를 실행합니다.

```bash
python easyocr_solution.py
```

4. 실행이 완료되면 `results_hybrid_easyocr.csv` 파일에 최종 추출 결과가 저장됩니다.

---

**✅ 요약:**  
본 하이브리드 솔루션은 OpenCV의 안정적인 금속판 탐지와 EasyOCR의 고정밀 인식 능력을 결합하여,  
복잡한 환경에서도 높은 OCR 신뢰도를 달성합니다.
