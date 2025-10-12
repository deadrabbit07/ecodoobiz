# 📚 EcoDoobiz 프로젝트 가이드

> **목적**: 초보 개발자 팀원들을 위한 Git & Markdown 사용 가이드  
> **팀 구성**: deadrabbit07, kwonhj0510, minjun824  
> **형식**: 개인 폴더별 `.md` 파일로 정리 및 공유  

---

## 📑 목차
1. [프로젝트 시작하기](#🚀-프로젝트-시작하기)
2. [GitHub 명령어 가이드](#🧭-github-명령어-가이드)
3. [문서 작성 규칙](#✍️-문서-작성-규칙)
4. [워크플로우](#🔄-워크플로우)
5. [문제 해결 가이드](#🧯-문제-해결-가이드)
6. [추천 도구](#🧰-추천-도구)
7. [참고 자료](#🔗-참고-자료)

---

## 🚀 프로젝트 시작하기

```bash
# 저장소 클론
git clone [저장소URL] ecodoobiz
cd ecodoobiz

# 개인 브랜치 생성
git checkout -b [본인이름]
git push -u origin [본인이름]
```

### 📂 폴더 구조 규칙
- 폴더명: GitHub 사용자명  
- 파일명: 영어 소문자 + `_` (예: `git_commands.md`)  
- 문서 순서: 목차 → 설명 → 예시 → 참고자료  

---

## 🧭 GitHub 명령어 가이드

### 🔧 기본 설정
```bash
git config --global user.name "이름"
git config --global user.email "이메일"
git config --global init.defaultBranch main
git config --global core.editor "vim"
git config --list
```

### 📦 저장소 관리
```bash
git init
git remote add origin [URL]
git remote -v
git remote rename origin new
git remote remove origin
```

### 🌿 브랜치 관리
```bash
git branch -a
git checkout -b feature/test
git switch branch-name
git branch -d old
git push origin --delete old
git branch -m old new
```

### 📝 커밋 관리
```bash
git status
git add .
git commit -m "메시지"
git log --oneline
git commit --amend -m "수정"
```

### 🔙 커밋 되돌리기
```bash
git reset --soft HEAD~1
git reset --hard HEAD~1
```

### 🔄 동기화 및 병합
```bash
git fetch origin
git pull origin main
git merge branch-name
git rebase main
```

⚠️ 충돌 발생 시:
```bash
git add .
git rebase --continue
```

### 🏷️ 태그 관리
```bash
git tag -a v1.0.0 -m "버전 1.0.0"
git tag
git push origin --tags
git push origin --delete v1.0.0
```

### 🧩 변경사항 관리
```bash
git diff
git rm filename
git mv old new
git stash
git stash pop
```

---

## ✍️ 문서 작성 규칙

### 📄 파일명 규칙
- 영어 소문자 + `_`
- 예: `github_commands.md`

### 📘 문서 기본 구조
1. 제목 / 개요  
2. 설명  
3. 예시  
4. 참고자료  

### 📋 예시
```markdown
# Git 명령어 정리

## 개요
- Git 기본 명령어 요약

## 명령어 예시
| 명령어 | 설명 | 예시 |
|--------|------|------|
| git add | 파일 스테이징 | `git add .` |
| git commit | 커밋 생성 | `git commit -m "메시지"` |

## 참고자료
- [Pro Git Book](https://git-scm.com/book)
```

---

## 🔄 워크플로우

### 🆕 새 문서 작성
```bash
git checkout -b feature/new-doc
touch [폴더명]/[파일명].md
git add .
git commit -m "Add: [문서명]"
git push origin feature/new-doc
```

### 🧱 문서 수정
```bash
git checkout main
git pull origin main
git checkout -b fix/update-doc
git add .
git commit -m "Fix: 수정 내용"
git push origin fix/update-doc
```

### 🔁 일일 루틴
```bash
git checkout main
git pull origin main
git checkout [개인브랜치]
git merge main
```

---

## 🧯 문제 해결 가이드

### 커밋을 잘못했을 때
```bash
git commit --amend -m "수정된 메시지"
git reset --soft HEAD~1
```

### 잘못된 브랜치에 커밋했을 때
```bash
git cherry-pick [커밋해시]
git reset --hard HEAD~1
```

### 충돌 발생 시
```bash
git fetch origin
git rebase origin/main
git add .
git rebase --continue
```

### 파일 복원
```bash
git checkout HEAD -- filename
```

---

## 🧰 추천 도구

### VS Code 확장
- Markdown All in One  
- GitLens  
- Git Graph  
- Markdown Preview Enhanced  

### 유용한 Git 별칭
```bash
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit
```

**사용 예시**
```bash
git st   # git status
git co main
```

---

## 🔗 참고 자료
- [Git 공식 문서](https://git-scm.com/doc)  
- [GitHub 가이드](https://docs.github.com/ko)  
- [Pro Git 책](https://git-scm.com/book/ko/v2)  
- [Markdown 가이드](https://www.markdownguide.org/basic-syntax/)  
- [Cursor AI](https://cursor.sh)
