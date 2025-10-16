# Git 명령어 가이드

## 기본 설정 (Configuration)

| 명령어 | 설명 |
| :-- | :-- |
| `git config --global user.name "사용자이름"` | Git에 사용자 이름을 설정합니다. (글로벌 적용) |
| `git config --global user.email "이메일주소"` | Git에 사용자 이메일을 설정합니다. (글로벌 적용) |
| `git config --global init.defaultBranch main` | 새 저장소 생성 시 기본 브랜치 이름을 main으로 설정합니다. |
| `git config --global core.editor "vim"` | Git 커밋 메시지 등을 작성할 때 사용할 기본 텍스트 편집기를 vim으로 설정합니다. |
| `git config --list` | 현재 설정된 모든 Git 환경 변수를 확인합니다. |

---

## 저장소 관리 (Repository Management)

| 명령어 | 설명 |
| :-- | :-- |
| `git init` | 현재 디렉토리를 Git 로컬 저장소로 초기화합니다. (.git 폴더 생성) |
| `git remote add origin [URL]` | 로컬 저장소에 원격 저장소(GitHub 등)를 연결하고, 별칭을 origin으로 지정합니다. |
| `git remote -v` | 현재 로컬 저장소에 연결된 원격 저장소 목록과 주소를 확인합니다. |
| `git remote rename origin new` | 연결된 원격 저장소의 별칭을 origin에서 new로 변경합니다. |
| `git remote remove origin` | 연결된 원격 저장소 중 origin 별칭의 연결을 제거합니다. |

---

## 브랜치 관리 (Branch Management)

| 명령어 | 설명 |
| :-- | :-- |
| `git branch` | 현재 존재하는 브랜치 목록을 확인합니다. |
| `git branch [브랜치명]` | 새 브랜치를 생성합니다. |
| `git switch [브랜치명]` | 지정한 브랜치로 전환합니다. |
| `git switch -c [브랜치명]` | 새 브랜치를 생성하고 바로 전환합니다. |
| `git branch -d [브랜치명]` | 병합된 브랜치를 안전하게 삭제합니다. |
| `git branch -D [브랜치명]` | 병합 여부와 상관없이 브랜치를 강제로 삭제합니다. |
| `git merge [브랜치명]` | 현재 브랜치에 다른 브랜치를 병합합니다. |
| `git diff [브랜치1] [브랜치2]` | 두 브랜치 간의 변경 사항을 비교합니다. |

---

## 커밋 및 변경 관리 (Commit & Changes)

| 명령어 | 설명 |
| :-- | :-- |
| `git add [파일명]` | 특정 파일을 스테이징 영역에 추가합니다. |
| `git add .` | 모든 변경된 파일을 스테이징 영역에 추가합니다. |
| `git commit -m "메시지"` | 스테이징된 변경 사항을 커밋합니다. |
| `git commit --amend` | 마지막 커밋 메시지나 내용을 수정합니다. |
| `git rm [파일명]` | 파일을 삭제하고 그 변경 사항을 커밋에 반영합니다. |
| `git mv [기존이름] [새이름]` | 파일 이름을 변경하고 Git에 반영합니다. |

---

## 원격 저장소와 동기화 (Push / Pull / Fetch / Merge)

| 명령어 | 설명 |
| :-- | :-- |
| `git push origin main` | 로컬 main 브랜치를 원격 저장소로 업로드합니다. |
| `git push -u origin [브랜치명]` | 새 브랜치를 원격 저장소에 올리고 추적 설정을 만듭니다. |
| `git pull origin main` | 원격 저장소의 변경사항을 가져와 로컬 main 브랜치에 병합합니다. |
| `git fetch origin` | 원격 저장소의 최신 변경사항을 가져오지만 병합은 하지 않습니다. |
| `git merge origin/main` | 가져온 원격 변경사항을 현재 브랜치에 병합합니다. |
| `git clone [URL]` | 원격 저장소를 로컬로 복제합니다. |

---

## 되돌리기 및 복구 (Reset / Revert / Restore)

| 명령어 | 설명 |
| :-- | :-- |
| `git reset --soft [커밋ID]` | 지정한 커밋으로 되돌리고, 변경 사항은 스테이징 상태로 유지합니다. |
| `git reset --mixed [커밋ID]` | 지정한 커밋으로 되돌리고, 변경 사항은 워킹 디렉토리에 남깁니다. |
| `git reset --hard [커밋ID]` | 지정한 커밋 시점으로 완전히 되돌립니다. (복구 불가 주의) |
| `git revert [커밋ID]` | 특정 커밋을 되돌리는 새로운 커밋을 생성합니다. |
| `git restore [파일명]` | 변경된 파일을 최근 커밋 상태로 되돌립니다. |
| `git restore --staged [파일명]` | 스테이징 영역에서 파일을 제외시킵니다. |

---

## 상태 확인 및 로그 (Status & Log)

| 명령어 | 설명 |
| :-- | :-- |
| `git status` | 현재 작업 디렉토리와 스테이징 상태를 확인합니다. |
| `git log` | 커밋 이력을 확인합니다. |
| `git log --oneline --graph --all` | 브랜치 구조를 그래프로 간단히 표시합니다. |
| `git show [커밋ID]` | 특정 커밋의 상세 변경 내용을 확인합니다. |
| `git diff` | 커밋 전 변경된 내용을 확인합니다. |
| `git blame [파일명]` | 파일의 각 줄이 어떤 커밋에서 변경되었는지 표시합니다. |

---

 **Tip:**  
- `--help` 옵션을 붙이면 각 명령어의 자세한 설명을 볼 수 있습니다.  
  예: `git commit --help`

---

