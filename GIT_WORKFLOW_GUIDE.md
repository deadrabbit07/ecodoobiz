# 🚀 EcoDoobiz 팀 Git Workflow 가이드

> **팀 구성**: deadrabbit07, kwonhj0510, minjun824 (3명)  
> **목적**: 효율적인 협업을 위한 Git Flow 전략

---

## 📋 추천 Git Flow 전략

### 🎯 **GitHub Flow** (추천)
3명 팀에 가장 적합한 간단하고 효율적인 전략입니다.

```
main (production)
├── feature/document-guide
├── feature/ai-prompts
└── feature/personal-notes
```

**장점**:
- 간단하고 직관적
- 빠른 배포 가능
- 리뷰 과정이 명확
- 3명 팀에 최적화

---

## 🌿 브랜치 전략

### 주요 브랜치
- **`main`**: 안정적인 메인 브랜치 (배포 가능한 상태)
- **`develop`**: 개발 통합 브랜치 (선택사항)

### 피처 브랜치 명명 규칙
```bash
# 개인 작업용
feature/[이름]/[작업내용]
# 예시:
feature/deadrabbit07/document-guide
feature/kwonhj0510/learning-notes
feature/minjun824/ai-prompts

# 공동 작업용
feature/[작업내용]
# 예시:
feature/project-structure
feature/git-workflow
```

---

## 🔄 워크플로우 상세 가이드

### 1️⃣ 초기 설정

```bash
# 1. 메인 저장소 클론
git clone [저장소URL] ecodoobiz
cd ecodoobiz

# 2. 개인 브랜치 생성 (각자 실행)
git checkout -b feature/[본인이름]/setup
git push -u origin feature/[본인이름]/setup

# 3. .gitignore 파일 생성
touch .gitignore
echo "*.DS_Store" >> .gitignore
echo ".vscode/" >> .gitignore
echo "*.log" >> .gitignore
```

### 2️⃣ 일상적인 작업 플로우

#### 새 기능/문서 작업 시작
```bash
# 1. 메인 브랜치 최신화
git checkout main
git pull origin main

# 2. 새 피처 브랜치 생성
git checkout -b feature/[이름]/[작업내용]
# 예시: git checkout -b feature/deadrabbit07/vi-commands

# 3. 작업 시작
```

#### 작업 중간 저장
```bash
# 변경사항 스테이징
git add .

# 의미있는 커밋 메시지로 저장
git commit -m "Add: Vi 명령어 정리 문서 추가"

# 원격에 푸시 (첫 푸시 시)
git push -u origin feature/deadrabbit07/vi-commands

# 이후 푸시
git push
```

#### 작업 완료 후
```bash
# 1. 최신 main과 동기화
git checkout main
git pull origin main
git checkout feature/[브랜치명]
git merge main

# 2. 충돌 해결 (있다면)
# 3. 최종 푸시
git push

# 4. GitHub에서 Pull Request 생성
```

### 3️⃣ Pull Request 생성 및 리뷰

#### PR 생성 시 체크리스트
- [ ] 제목: 명확한 작업 내용
- [ ] 설명: 변경사항 요약
- [ ] 리뷰어 지정 (최소 1명)
- [ ] 관련 이슈 연결 (있다면)

#### PR 제목 규칙
```
Add: 새로운 기능 추가
Fix: 버그 수정
Update: 기존 내용 수정
Docs: 문서 작업
Refactor: 코드 리팩토링
```

#### 리뷰어 규칙
- **자신의 PR**: 다른 팀원 1명이 리뷰
- **공동 작업**: 모든 팀원이 리뷰
- **문서 작업**: 간단한 내용은 바로 머지 가능

---

## 🛠️ 실제 사용 예시

### 시나리오 1: 개인 문서 작업

```bash
# deadrabbit07이 Vi 명령어 정리 문서 작업
git checkout main
git pull origin main
git checkout -b feature/deadrabbit07/vi-commands

# 문서 작성 후
git add .
git commit -m "Add: Vi/Vim 명령어 완전 정리 가이드"
git push -u origin feature/deadrabbit07/vi-commands

# GitHub에서 PR 생성 → kwonhj0510이 리뷰 → 머지
```

### 시나리오 2: 프로젝트 구조 변경

```bash
# 3명이 함께 프로젝트 구조 개선
git checkout main
git pull origin main
git checkout -b feature/project-restructure

# 각자 담당 부분 작업 후
git add .
git commit -m "Refactor: 프로젝트 폴더 구조 개선 및 README 추가"
git push -u origin feature/project-restructure

# GitHub에서 PR 생성 → 모든 팀원 리뷰 → 머지
```

### 시나리오 3: 버그 수정

```bash
# 기존 문서의 오타 발견
git checkout main
git pull origin main
git checkout -b fix/typo-in-git-guide

# 수정 후
git add .
git commit -m "Fix: Git 명령어 예시 오타 수정"
git push -u origin fix/typo-in-git-guide

# 즉시 PR 생성 → 빠른 리뷰 → 머지
```

---

## 📅 주간 워크플로우

### 월요일: 주간 계획
```bash
# 각자 이번 주 작업 계획 브랜치 생성
git checkout -b feature/[이름]/week-[주차]
# 예시: feature/deadrabbit07/week-1
```

### 평일: 일상 작업
```bash
# 매일 아침
git checkout main && git pull origin main

# 작업 시작 전
git checkout feature/[브랜치명]
git merge main  # 필요시

# 작업 중간중간
git add . && git commit -m "WIP: [작업내용]"
git push
```

### 금요일: 주간 정리
```bash
# 완료된 작업들 PR 생성
# 미완성 작업은 다음 주로 연기
```

---

## 🚨 충돌 해결 가이드

### 일반적인 충돌 상황
```bash
# 충돌 발생 시
git checkout feature/my-branch
git merge main

# 충돌 파일 확인
git status

# 충돌 해결 (에디터에서)
# <<<<<<< HEAD
# 내 변경사항
# =======
# 다른 사람 변경사항
# >>>>>>> main

# 해결 후
git add .
git commit -m "Resolve: merge conflict in [파일명]"
git push
```

### 복잡한 충돌 시
```bash
# 리베이스로 깔끔하게 정리
git rebase main

# 충돌 해결 후
git add .
git rebase --continue

# 강제 푸시 (주의!)
git push --force-with-lease
```

---

## 🔧 유용한 Git 설정

### Git 별칭 설정 (각자 설정)
```bash
# 편의를 위한 별칭들
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit
git config --global alias.unstage 'reset HEAD --'
git config --global alias.last 'log -1 HEAD'
git config --global alias.visual '!gitk'

# 사용 예시
git st    # git status
git co main    # git checkout main
git br    # git branch
```

### 자주 사용하는 명령어 조합
```bash
# 빠른 작업 시작
alias gstart='git checkout main && git pull origin main && git checkout -b'

# 작업 완료
alias gdone='git add . && git commit -m "WIP" && git push'

# 브랜치 정리
alias gclean='git branch --merged | grep -v "\*\|main" | xargs -n 1 git branch -d'
```

---

## 📋 팀 규칙 및 약속

### 커밋 메시지 규칙
```
[타입]: [간단한 설명]

- Add: 새로운 기능/문서 추가
- Fix: 버그 수정
- Update: 기존 내용 수정
- Remove: 삭제
- Docs: 문서 작업
- Style: 포맷팅, 세미콜론 등
- Refactor: 코드 리팩토링
- Test: 테스트 추가/수정
```

### 브랜치 정리 규칙
- **매주 금요일**: 사용하지 않는 브랜치 정리
- **PR 머지 후**: 해당 브랜치 삭제
- **로컬 정리**: `git branch --merged | grep -v main | xargs git branch -d`

### 리뷰 규칙
- **24시간 내**: PR 리뷰 완료
- **긍정적 피드백**: 건설적인 코멘트
- **승인 조건**: 최소 1명의 승인 필요

---

## 🚀 초기 설정 체크리스트

### 1단계: 저장소 준비
- [ ] GitHub 저장소 생성
- [ ] README.md 작성
- [ ] .gitignore 파일 추가
- [ ] 초기 커밋 및 푸시

### 2단계: 팀원 초대
- [ ] 각 팀원을 Collaborator로 추가
- [ ] 브랜치 보호 규칙 설정 (선택사항)

### 3단계: 개인 설정
- [ ] Git 사용자 정보 설정
- [ ] SSH 키 설정 (선택사항)
- [ ] 편의 별칭 설정

### 4단계: 첫 작업
- [ ] 각자 개인 폴더 작업 브랜치 생성
- [ ] 기본 문서 작성
- [ ] 첫 PR 생성 및 리뷰

---

## 💡 팀 운영 팁

### 소통 방법
- **GitHub Issues**: 작업 계획 및 버그 추적
- **PR 코멘트**: 코드 리뷰 및 토론
- **커밋 메시지**: 작업 내용 명확히 기록

### 효율성 향상
- **작은 단위 작업**: 한 번에 하나씩
- **자주 커밋**: 작업 중간중간 저장
- **명확한 PR**: 변경사항 명확히 설명

### 문제 예방
- **정기 동기화**: 매일 main 브랜치 업데이트
- **충돌 예방**: 같은 파일 동시 작업 피하기
- **백업**: 중요한 작업은 로컬 백업

---

## 📞 문제 해결

### 자주 발생하는 상황

**Q: 다른 사람이 내 파일을 수정했어요**
```bash
# 최신 상태로 동기화
git checkout main
git pull origin main
git checkout feature/my-branch
git merge main
# 충돌 해결 후 계속 작업
```

**Q: 잘못된 브랜치에 커밋했어요**
```bash
# 커밋을 올바른 브랜치로 이동
git checkout target-branch
git cherry-pick commit-hash
git checkout wrong-branch
git reset --hard HEAD~1
```

**Q: PR을 잘못 만들었어요**
```bash
# 브랜치 이름 변경
git branch -m old-name new-name
git push origin new-name
git push origin --delete old-name
# GitHub에서 PR 재생성
```

---

## 🎯 다음 단계

1. **이 가이드 검토**: 팀원들과 함께 읽어보기
2. **규칙 조정**: 팀 상황에 맞게 수정
3. **초기 설정**: 저장소 생성 및 첫 설정
4. **실전 연습**: 작은 작업으로 워크플로우 익히기
5. **지속 개선**: 사용하면서 불편한 점 개선

---

**💡 기억하세요**: 완벽한 Git Flow보다는 **팀이 편하게 사용할 수 있는 방법**이 가장 좋습니다. 시작은 간단하게 하고, 필요에 따라 점진적으로 개선해나가세요!
