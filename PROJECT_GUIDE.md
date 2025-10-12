# 📚 EcoDoobiz 프로젝트 가이드

> **목적**: 노션 대신 개인 폴더별 마크다운 파일로 문서 정리하기  
> **팀**: deadrabbit07, kwonhj0510, minjun824

---

## 📁 프로젝트 구조

```
ecodoobiz/
├── deadrabbit07/           # 개발 관련 문서
│   ├── claude_prompt.md    # Claude AI 프롬프트 (Odoo 개발용)
│   ├── gpt_prompt.md       # GPT 프롬프트 (Odoo 개발용)
│   ├── using_ai.md         # AI 도구 사용법 정리
│   └── vi_commands.md      # Vi/Vim 명령어 정리
├── kwonhj0510/             # 개인 문서
│   └── example.md          # 예시 문서
├── minjun824/              # 개인 문서
│   └── gpt_prompt          # 프롬프트 파일
└── README.md               # 프로젝트 메인 문서
```

---

## 🚀 빠른 시작 가이드

### 1. 프로젝트 클론 및 설정
```bash
# 저장소 클론
git clone [저장소URL] ecodoobiz
cd ecodoobiz

# 개인 브랜치 생성 및 이동
git checkout -b [본인이름]
git push -u origin [본인이름]

# 작업 시작
```

### 2. 문서 작성 규칙
- **파일명**: 영어 소문자, 언더스코어 사용 (예: `github_commands.md`)
- **폴더명**: GitHub 사용자명 사용
- **문서 구조**: 목차, 설명, 예시, 참고자료 순서로 작성

---

## 📖 GitHub 명령어 완전 가이드

### 🔧 기본 설정

```bash
# Git 사용자 정보 설정
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# 기본 에디터 설정 (macOS)
git config --global core.editor "vim"

# 기본 브랜치명 설정
git config --global init.defaultBranch main

# 현재 설정 확인
git config --list
```

### 📂 저장소 관리

```bash
# 새 저장소 초기화
git init

# 원격 저장소 연결
git remote add origin [저장소URL]

# 원격 저장소 확인
git remote -v

# 원격 저장소 이름 변경
git remote rename origin new-name

# 원격 저장소 제거
git remote remove origin
```

### 🌿 브랜치 관리

```bash
# 브랜치 목록 확인
git branch                    # 로컬 브랜치
git branch -r                 # 원격 브랜치
git branch -a                 # 모든 브랜치

# 새 브랜치 생성 및 이동
git checkout -b feature/new-feature
git switch -c feature/new-feature    # Git 2.23+ 버전

# 브랜치 이동
git checkout branch-name
git switch branch-name               # Git 2.23+ 버전

# 브랜치 삭제
git branch -d branch-name           # 로컬 브랜치 삭제
git branch -D branch-name           # 강제 삭제
git push origin --delete branch-name  # 원격 브랜치 삭제

# 브랜치 이름 변경
git branch -m old-name new-name
```

### 📝 커밋 관리

```bash
# 파일 상태 확인
git status

# 파일 스테이징
git add filename                  # 특정 파일
git add .                        # 모든 변경사항
git add -A                       # 삭제된 파일까지 포함

# 커밋 생성
git commit -m "커밋 메시지"
git commit -am "파일 추가 후 바로 커밋"

# 커밋 히스토리 확인
git log --oneline               # 간단한 히스토리
git log --graph                 # 그래프 형태
git log --author="사용자명"      # 특정 사용자 커밋

# 커밋 메시지 수정 (마지막 커밋)
git commit --amend -m "새로운 메시지"

# 커밋 되돌리기
git reset --soft HEAD~1         # 커밋 취소, 변경사항 유지
git reset --mixed HEAD~1        # 커밋 취소, 스테이징 취소
git reset --hard HEAD~1         # 커밋 취소, 변경사항 삭제
```

### 🔄 동기화 및 병합

```bash
# 원격 저장소에서 최신 변경사항 가져오기
git fetch origin
git pull origin main

# 다른 브랜치와 병합
git merge branch-name

# 리베이스 (히스토리 정리)
git rebase main
git rebase -i HEAD~3            # 최근 3개 커밋 대화형 리베이스

# 충돌 해결 후 계속
git add .
git rebase --continue
```

### 🚀 푸시 및 풀

```bash
# 원격 저장소에 푸시
git push origin branch-name
git push -u origin branch-name  # 첫 푸시 시 upstream 설정

# 강제 푸시 (주의!)
git push --force origin branch-name
git push --force-with-lease origin branch-name  # 안전한 강제 푸시

# 원격 저장소에서 풀
git pull origin branch-name
git fetch origin && git merge origin/branch-name  # fetch + merge
```

### 🔍 파일 및 변경사항 관리

```bash
# 파일 변경사항 확인
git diff                        # 스테이징되지 않은 변경사항
git diff --staged              # 스테이징된 변경사항
git diff HEAD~1                # 이전 커밋과 비교

# 파일 삭제
git rm filename                # 파일 삭제 및 스테이징
git rm --cached filename       # Git에서만 삭제, 로컬 유지

# 파일 이동/이름 변경
git mv old-name new-name

# 변경사항 임시 저장
git stash                      # 변경사항 임시 저장
git stash list                 # 저장된 스태시 목록
git stash pop                  # 최근 스태시 적용 후 삭제
git stash apply                # 스태시 적용, 저장 유지
git stash drop                 # 스태시 삭제
```

### 🏷️ 태그 관리

```bash
# 태그 생성
git tag v1.0.0                 # 경량 태그
git tag -a v1.0.0 -m "버전 1.0.0"  # 주석 태그

# 태그 목록
git tag

# 태그 푸시
git push origin v1.0.0
git push origin --tags         # 모든 태그 푸시

# 태그 삭제
git tag -d v1.0.0              # 로컬 태그 삭제
git push origin --delete v1.0.0  # 원격 태그 삭제
```

### 🔧 고급 명령어

```bash
# 특정 커밋으로 이동
git checkout commit-hash
git checkout branch-name       # 브랜치로 복귀

# 파일 특정 버전 복원
git checkout HEAD~1 -- filename

# 커밋 해시 찾기
git log --oneline --grep="검색어"

# 원격 저장소 URL 변경
git remote set-url origin [새URL]

# Git 무시 파일 설정
echo "*.log" >> .gitignore
echo "node_modules/" >> .gitignore
```

---

## 📝 마크다운 작성 가이드

### 기본 문법

```markdown
# 제목 1
## 제목 2
### 제목 3

**굵은 글씨**
*기울임*
~~취소선~~

- 순서 없는 목록
- 항목 2

1. 순서 있는 목록
2. 항목 2

[링크](https://example.com)
![이미지](image.png)

`인라인 코드`
```

### 코드 블록

```markdown
```python
# Python 코드 예시
def hello():
    print("Hello, World!")
```

```bash
# Bash 명령어 예시
git add .
git commit -m "Update documentation"
```
```

### 표 작성

```markdown
| 명령어 | 설명 | 예시 |
|--------|------|------|
| git add | 파일 스테이징 | git add . |
| git commit | 커밋 생성 | git commit -m "메시지" |
```

### 체크리스트

```markdown
- [x] 완료된 작업
- [ ] 진행 중인 작업
- [ ] 예정된 작업
```

---

## 🛠️ 유용한 도구 및 확장

### VS Code 확장 추천
- **Markdown All in One**: 마크다운 편집 도구
- **GitLens**: Git 히스토리 및 정보 표시
- **Git Graph**: 브랜치 시각화
- **Markdown Preview Enhanced**: 마크다운 미리보기

### 터미널 도구
```bash
# Git 별칭 설정
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit

# 사용 예시
git st    # git status
git co main    # git checkout main
```

---

## 📋 문서 작성 템플릿

### 개인 문서 템플릿
```markdown
# [주제] 정리

## 개요
- 목적: 
- 사용 환경: 
- 작성일: 

## 기본 개념
### 핵심 용어
- 

### 주요 특징
- 

## 사용법
### 1. 기본 설정
```bash
# 명령어 예시
```

### 2. 실제 사용
```bash
# 실제 명령어
```

## 예시
```code
# 코드 예시
```

## 주의사항
- ⚠️ 주의할 점
- 💡 팁

## 참고 자료
- [링크](URL)
```

### 명령어 정리 템플릿
```markdown
# [도구명] 명령어 정리

## 기본 명령어
| 명령어 | 설명 | 예시 |
|--------|------|------|
| cmd1 | 설명 | `cmd1 example` |

## 자주 사용하는 조합
```bash
# 조합 명령어
cmd1 && cmd2
```

## 문제 해결
### 자주 발생하는 에러
**에러 메시지**: `error message`
**해결방법**: 
1. 단계 1
2. 단계 2
```

---

## 🔄 워크플로우

### 1. 새 문서 작성 시
```bash
# 1. 브랜치 생성 및 이동
git checkout -b feature/new-document

# 2. 문서 작성
touch [폴더명]/[파일명].md

# 3. 커밋 및 푸시
git add .
git commit -m "Add: [문서명] 정리"
git push origin feature/new-document

# 4. Pull Request 생성 (GitHub에서)
```

### 2. 문서 수정 시
```bash
# 1. 최신 상태로 동기화
git checkout main
git pull origin main

# 2. 수정 브랜치 생성
git checkout -b fix/update-document

# 3. 수정 후 커밋
git add .
git commit -m "Fix: [수정내용]"
git push origin fix/update-document
```

### 3. 일일 작업 플로우
```bash
# 아침에 시작할 때
git checkout main
git pull origin main
git checkout [개인브랜치]
git merge main

# 작업 중간중간
git add .
git commit -m "WIP: 작업 중간 저장"

# 작업 완료 후
git push origin [개인브랜치]
```

---

## 📚 각 폴더별 문서 가이드

### deadrabbit07/ (개발 관련)
- **claude_prompt.md**: Claude AI 프롬프트 (Odoo 개발용)
- **gpt_prompt.md**: GPT 프롬프트 (Odoo 개발용)  
- **using_ai.md**: AI 도구 사용법 정리
- **vi_commands.md**: Vi/Vim 명령어 정리

### kwonhj0510/ (개인 문서)
- 자유롭게 개인 학습 내용 정리
- 예시: `example.md`

### minjun824/ (개인 문서)
- 자유롭게 개인 학습 내용 정리
- 예시: `gpt_prompt`

---

## 🚨 주의사항 및 모범 사례

### Git 사용 시 주의사항
- **절대 하지 말 것**: `git push --force` (팀 작업 시)
- **커밋 메시지**: 명확하고 간결하게 작성
- **브랜치명**: 의미있는 이름 사용 (예: `feature/add-login`)
- **작업 전**: 항상 최신 상태로 동기화

### 문서 작성 시 주의사항
- **파일명**: 영어 소문자, 언더스코어 사용
- **목차**: 항상 목차를 먼저 작성
- **예시**: 실제 실행 가능한 예시 제공
- **정기 업데이트**: 내용이 변경되면 문서도 업데이트

### 협업 시 주의사항
- **개인 브랜치**: 각자 개인 브랜치에서 작업
- **충돌 해결**: 충돌 발생 시 팀원과 소통
- **리뷰**: Pull Request 생성 후 리뷰 요청

---

## 📞 문제 해결 가이드

### 자주 발생하는 Git 문제

**Q: 커밋을 잘못했어요**
```bash
# 마지막 커밋 메시지 수정
git commit --amend -m "새로운 메시지"

# 마지막 커밋 취소 (변경사항 유지)
git reset --soft HEAD~1
```

**Q: 잘못된 브랜치에 커밋했어요**
```bash
# 커밋을 올바른 브랜치로 이동
git checkout target-branch
git cherry-pick commit-hash
git checkout wrong-branch
git reset --hard HEAD~1
```

**Q: 원격 저장소와 충돌이 발생했어요**
```bash
# 최신 상태로 동기화
git fetch origin
git rebase origin/main
# 충돌 해결 후
git add .
git rebase --continue
```

**Q: 파일을 실수로 삭제했어요**
```bash
# Git에서 삭제된 파일 복원
git checkout HEAD -- filename

# 스테이징되지 않은 변경사항 복원
git checkout -- filename
```

---

## 🔗 유용한 링크

### Git 관련
- [Git 공식 문서](https://git-scm.com/doc)
- [GitHub 가이드](https://guides.github.com/)
- [Pro Git 책](https://git-scm.com/book)

### 마크다운 관련
- [마크다운 가이드](https://www.markdownguide.org/)
- [마크다운 치트시트](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)

### 개발 도구
- [VS Code](https://code.visualstudio.com/)
- [Cursor](https://cursor.sh/)

---

## 📝 업데이트 로그

| 날짜 | 업데이트 내용 | 작성자 |
|------|---------------|--------|
| 2024-01-XX | 초기 프로젝트 가이드 작성 | - |

---

**💡 팁**: 이 문서는 팀원들이 자주 참조할 수 있도록 작성되었습니다. 새로운 내용이나 수정사항이 있으면 언제든 업데이트해주세요!
