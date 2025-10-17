# 🧭 Git 명령어 정리

---

## 1. 기본 설정

| 명령어 | 상황 |
| --- | --- |
| `git -v` | Git 버전 확인 |
| `git config --global user.name '<이름>'` | 사용자 이름 설정 |
| `git config --global user.email '<이메일>'` | 사용자 이메일 설정 |
| `git config --list` | 설정 확인 |

---

## 2. 로컬 저장소 관리 / init

| 명령어 | 상황 |
| --- | --- |
| `git init` | 새로운 Git 저장소 초기화 |
| `git clone <URL>` | Git Clone |
| `git status` | 변경사항 확인 |
| `git add <파일명>` | 특정 파일 스테이징 |
| `git add .` | 모든 파일 스테이징 |
| `git rm <파일명>` | 파일 삭제 후 스테이징 (실제로 파일이 사라짐) |
| `git rm --cached <파일명>` | 로컬 파일은 남기고 Git에서만 제거 후 스테이징 |
| `git remote` | 원격 저장소 목록 확인 |

---

## 3. 커밋 (Commit)

| 명령어 | 상황 |
| --- | --- |
| `git commit -m '커밋 메세지'` | 커밋 생성 |
| `git commit -am '커밋 메세지'` | add + commit 동시에 |
| `git commit --amend` | 최근 커밋 수정 |
| `git log` | 커밋 내역 확인 |
| `git log --oneline` | 커밋 내역 한줄로 확인 (요약) |
| `git show <커밋ID>` | 특정 커밋 내용 확인 |

---

## 4. 브랜치 (Branch)

| 명령어 | 상황 |
| --- | --- |
| `git branch` | 브랜치 목록 보기 |
| `git branch <브랜치명>` | 새 브랜치 생성 |
| `git checkout <브랜치명>` | 브랜치 이동 |
| `git switch <브랜치명>` | 브랜치 이동 (추천) |
| `git switch -c <브랜치명>` | 브랜치 생성 + 이동 |
| `git merge <브랜치명>` | 현재 브랜치에 다른 브랜치 병합 |
| `git branch -d <브랜치명>` | 브랜치 삭제 |
| `git branch -m <새이름>` | 브랜치 이름 변경 |

---

## 5. 원격 저장소 (Remote)

| 명령어 | 상황 |
| --- | --- |
| `git remote add origin <URL>` | 원격 저장소 등록 |
| `git remote -v` | 원격 저장소 URL 확인 |
| `git push -u origin <브랜치명>` | 브랜치를 원격에 처음 푸시 (이후 기본으로 설정됨) |
| `git push` | 기본 원격 브랜치에 푸시 |
| `git push origin <브랜치명>` | 특정 브랜치에 푸시 |
| `git pull` | 원격 변경사항 가져오기 + 병합 |
| `git fetch` | 원격 변경사항만 가져오기 |
| `git remote remove origin` | 원격 저장소 연결 해제 |

---

## 6. 병합 & 충돌 (Merge & Conflict)

| 명령어 | 상황 |
| --- | --- |
| `git merge <브랜치명>` | 브랜치 병합 |

### ⚠️ 충돌 발생 시 해결 방법

1. 충돌 파일 열어 수정  
2. `git add <파일명>` 실행  
3. `git commit` 실행

### 🔧 충돌 해결 단축 팁

| 명령어 | 상황 |
| --- | --- |
| `git merge --abort` | 병합 취소 |
| `git reset --merge` | 병합 전 상태로 되돌리기 |

---

## 7. 되돌리기 (Reset & Revert)

| 명령어 | 상황 |
| --- | --- |
| `git reset <커밋ID>` | 특정 커밋으로 이동 (기록 남음) |
| `git reset --hard <커밋ID>` | 특정 커밋으로 완전히 되돌림 (주의!) |
| `git revert <커밋ID>` | 이전 커밋을 취소하고 새 커밋 생성 |
| `git revert --no-commit` | 이전 커밋을 취소하지만 커밋은 생성 안 함 |
| `git checkout -- <파일명>` | 마지막 커밋 상태로 되돌림 (작업 디렉토리 변경사항 취소) |

---

## 8. 스테이징 / 임시저장 (Stash)

> `git stash`는 현재 변경사항을 임시로 저장하고 작업 디렉토리를 깨끗하게 만드는 명령어입니다.  
> 다른 브랜치로 이동하거나 다른 작업을 해야 할 때 유용합니다.  
> 나중에 `git stash pop`으로 복원할 수 있습니다.

| 명령어 | 상황 |
| --- | --- |
| `git stash` | 현재 작업 임시 저장 |
| `git stash list` | 임시 저장 목록 확인 |
| `git stash pop` | 마지막 stash 복원 + 삭제 |
| `git stash apply` | stash 복원 (삭제 안 함) |
| `git stash drop` | 특정 stash 삭제 |
| `git stash clear` | 모든 stash 삭제 |

---

## 9. 비교 (Diff)

> `git diff`는 **현재 작업 디렉토리**와  
> **Git이 추적 중인 최신 커밋(HEAD)** 을 비교하여  
> **변경된 내용의 차이점**을 보여줍니다.

| 명령어 | 상황 |
| --- | --- |
| `git diff` | 작업 디렉토리 vs 스테이징 비교 |
| `git diff <파일명>` | 특정 파일 비교 |
| `git diff --staged` | 스테이징된 파일과 이전 커밋 비교 |
| `git diff <커밋ID1> <커밋ID2>` | 두 커밋 비교 |
| `git diff <브랜치1> <브랜치2>` | 두 브랜치 비교 |

---

## 10. 태그 (Tag)

> `git tag`는 특정 커밋에 이름표를 붙이는 기능입니다.  
> 보통 **버전 관리나 중요한 시점 표시**에 사용됩니다.

| 명령어 | 상황 |
| --- | --- |
| `git tag` | 태그 목록 보기 |
| `git tag <태그명>` | 태그 생성 |
| `git tag -a <태그명> -m "메세지"` | 주석 포함 태그 생성 |
| `git show <태그명>` | 태그 상세 보기 |
| `git push origin <태그명>` | 원격에 특정 태그 푸시 |
| `git push origin --tags` | 모든 태그 푸시 |
| `git tag -d <태그명>` | 태그 삭제 |

---

## 11. 되돌림 및 복구 심화

| 명령어 | 상황 |
| --- | --- |
| `git reflog` | 모든 브랜치/커밋 이동 내역 보기 |
| `git checkout` | 특정 시점으로 이동 |
| `git restore` | 수정 취소 (최신 Git) |
| `git restore --staged <파일명>` | 스테이징 취소 |

---

## 12. 정리 및 유지보수

| 명령어 | 상황 |
| --- | --- |
| `git gc` | 저장소 최적화 |
| `git prune` | 불필요한 참조 삭제 |
| `git clean -fd` | 추적되지 않은 파일/폴더 삭제 |

---

📘 **참고**  
- `--` (en dash)가 아닌 `--`(double hyphen)를 반드시 사용해야 합니다.  
- 예: `git config --global`, `git rm --cached`, `git merge --abort`
