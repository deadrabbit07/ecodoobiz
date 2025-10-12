# 📚 EcoDoobiz 프로젝트 가이드

> **목적**: 초보 개발자 팀원들을 위한 Git & Markdown 사용 가이드  
> **팀 구성**: deadrabbit07, kwonhj0510, minjun824  
> **형식**: 개인 폴더별 `.md` 파일로 정리 및 공유  

---

## 📑 목차
1. [프로젝트 시작하기](#-프로젝트-시작하기)
2. [GitHub 명령어 가이드](#-github-명령어-가이드)
3. [문서 작성 규칙](#-문서-작성-규칙)
4. [워크플로우](#-워크플로우)
5. [문제 해결 가이드](#-문제-해결-가이드)
6. [추천 도구](#-추천-도구)
7. [참고 자료](#-참고-자료)

---

## 🚀 프로젝트 시작하기


# 저장소 클론
git clone [저장소URL] ecodoobiz
cd ecodoobiz

# 개인 브랜치 생성
git checkout -b [본인이름]
git push -u origin [본인이름]
📂 폴더 구조 규칙

폴더명: GitHub 사용자명

파일명: 영어 소문자 + _ (예: git_commands.md)

문서 순서: 목차 → 설명 → 예시 → 참고자료

## 🧭 GitHub 명령어 가이드
🔧 기본 설정
bash
코드 복사
git config --global user.name "이름"
git config --global user.email "이메일"
git config --global init.defaultBranch main
git config --global core.editor "vim"
git config --list
📦 저장소 관리
bash
코드 복사
git init                       # 새 저장소 생성
git remote add origin [URL]    # 원격 저장소 연결
git remote -v                  # 연결 확인
git remote rename origin new   # 이름 변경
git remote remove origin       # 연결 제거
🌿 브랜치 관리
bash
코드 복사
git branch -a                  # 브랜치 목록
git checkout -b feature/test   # 새 브랜치 생성
git switch branch-name         # 브랜치 이동
git branch -d old              # 로컬 삭제
git push origin --delete old   # 원격 삭제
git branch -m old new          # 이름 변경
📝 커밋 관리
bash
코드 복사
git status                     # 변경 확인
git add .                      # 전체 스테이징
git commit -m "메시지"          # 커밋
git log --oneline              # 커밋 목록
git commit --amend -m "수정"    # 마지막 커밋 수정
🔙 커밋 되돌리기

bash
코드 복사
git reset --soft HEAD~1        # 커밋 취소 (변경 유지)
git reset --hard HEAD~1        # 커밋+변경 삭제
🔄 동기화 및 병합
bash
코드 복사
git fetch origin               # 원격 변경사항 가져오기
git pull origin main           # main 최신화
git merge branch-name          # 병합
git rebase main                # 리베이스
⚠️ 충돌 발생 시:

bash
코드 복사
git add .
git rebase --continue
🏷️ 태그 관리
bash
코드 복사
git tag -a v1.0.0 -m "버전 1.0.0"
git tag                       # 목록 보기
git push origin --tags         # 모든 태그 푸시
git push origin --delete v1.0.0 # 원격 삭제
🧩 변경사항 관리
bash
코드 복사
git diff                       # 변경 비교
git rm filename                # 파일 삭제
git mv old new                 # 파일 이름 변경
git stash                      # 임시 저장
git stash pop                  # 복원
✍️ 문서 작성 규칙
파일명 규칙

영어 소문자 + _

예: github_commands.md

문서 기본 구조

제목 / 개요

설명

예시

참고자료

📘 예시

markdown
코드 복사
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
🔄 워크플로우
새 문서 작성
bash
코드 복사
git checkout -b feature/new-doc
touch [폴더명]/[파일명].md
git add .
git commit -m "Add: [문서명]"
git push origin feature/new-doc
문서 수정
bash
코드 복사
git checkout main
git pull origin main
git checkout -b fix/update-doc
git add .
git commit -m "Fix: 수정 내용"
git push origin fix/update-doc
일일 루틴
bash
코드 복사
git checkout main
git pull origin main
git checkout [개인브랜치]
git merge main
🧯 문제 해결 가이드
커밋을 잘못했을 때

bash
코드 복사
git commit --amend -m "수정된 메시지"
git reset --soft HEAD~1
잘못된 브랜치에 커밋했을 때

bash
코드 복사
git cherry-pick [커밋해시]
git reset --hard HEAD~1
충돌 발생 시

bash
코드 복사
git fetch origin
git rebase origin/main
git add .
git rebase --continue
파일 복원

bash
코드 복사
git checkout HEAD -- filename
🧰 추천 도구
VS Code 확장

Markdown All in One

GitLens

Git Graph

Markdown Preview Enhanced

유용한 Git 별칭

bash
코드 복사
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit

# 사용 예시
git st   # git status
git co main
🔗 참고 자료
Git 공식 문서

GitHub 가이드

Pro Git 책

Markdown 가이드

Cursor