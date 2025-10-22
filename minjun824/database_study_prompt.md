# 🗄️ SQL 문법 구분 정리 (DML / DDL / DCL)

SQL(Structured Query Language)은 데이터베이스를 조작하고 관리하기 위한 언어로, 역할에 따라 **DML**, **DDL**, **DCL** 세 가지로 구분된다.

---

## 🧩 1. DML (Data Manipulation Language)
> **데이터 조작 언어**  
> 실제 데이터(행, 레코드)를 추가·수정·삭제·조회할 때 사용한다.  
> 즉, **테이블의 구조가 아닌 데이터 자체를 다루는 명령어**이다.

| 명령어 | 설명 | 예시 |
|--------|------|------|
| `SELECT` | 데이터 조회 | `SELECT * FROM users;` |
| `INSERT` | 새로운 데이터 추가 | `INSERT INTO users (name, age) VALUES ('민준', 25);` |
| `UPDATE` | 기존 데이터 수정 | `UPDATE users SET age = 26 WHERE name = '민준';` |
| `DELETE` | 데이터 삭제 | `DELETE FROM users WHERE age < 20;` |

🟢 **특징**
- 트랜잭션(Transaction)과 밀접한 관련이 있음  
- 주로 **CRUD(Create, Read, Update, Delete)** 작업에 해당  
- `COMMIT`, `ROLLBACK`으로 작업을 확정하거나 되돌릴 수 있음

---

## 🧱 2. DDL (Data Definition Language)
> **데이터 정의 언어**  
> 데이터베이스의 **구조(스키마, 테이블, 컬럼 등)를 생성, 변경, 삭제**할 때 사용한다.  
> 즉, **데이터의 틀을 만드는 언어**이다.

| 명령어 | 설명 | 예시 |
|--------|------|------|
| `CREATE` | 데이터베이스 객체 생성 | `CREATE TABLE users (id SERIAL PRIMARY KEY, name TEXT);` |
| `ALTER` | 구조 변경 (컬럼 추가/삭제 등) | `ALTER TABLE users ADD COLUMN email TEXT;` |
| `DROP` | 객체 삭제 | `DROP TABLE users;` |
| `TRUNCATE` | 테이블의 모든 데이터 삭제 (구조는 유지) | `TRUNCATE TABLE users;` |

🔵 **특징**
- 실행 시 자동으로 **COMMIT** 처리됨 (되돌릴 수 없음)  
- **데이터의 틀 자체를 다룸**

---

## 🔐 3. DCL (Data Control Language)
> **데이터 제어 언어**  
> 사용자 권한을 부여하거나 회수하여 **데이터 접근을 제어**한다.

| 명령어 | 설명 | 예시 |
|--------|------|------|
| `GRANT` | 권한 부여 | `GRANT SELECT, INSERT ON users TO 'minjun';` |
| `REVOKE` | 권한 회수 | `REVOKE INSERT ON users FROM 'minjun';` |

🟣 **특징**
- 보안 및 접근 제어와 관련 있음  
- 주로 **관리자(DBA)** 가 사용  
- 권한을 통한 데이터 접근 제한을 구현

---

## 📚 요약 비교

| 구분 | 의미 | 주요 역할 | 예시 명령어 |
|------|------|------------|--------------|
| **DML** | 데이터 조작 | 데이터 추가/수정/삭제/조회 | `SELECT`, `INSERT`, `UPDATE`, `DELETE` |
| **DDL** | 데이터 정의 | 구조 생성/변경/삭제 | `CREATE`, `ALTER`, `DROP`, `TRUNCATE` |
| **DCL** | 데이터 제어 | 접근 권한 관리 | `GRANT`, `REVOKE` |

---

## 🧠 함께 알면 좋은 개념
- **Transaction (트랜잭션)**: DML 작업을 묶어서 한 단위로 처리 (예: 은행 송금 시)
- **Constraint (제약 조건)**: 데이터 무결성을 보장 (`PRIMARY KEY`, `FOREIGN KEY` 등)
- **Schema (스키마)**: 데이터베이스 구조를 정의한 설계도

---

✅ **학습 순서 추천**
1. DDL로 **테이블 구조 설계**  
2. DML로 **데이터 조작 및 조회 연습**  
3. DCL로 **권한 제어 및 보안 학습**

---

📍 **실습 팁 (PostgreSQL + pgAdmin)**
- `CREATE DATABASE practice_db;`  
- `CREATE TABLE users (id SERIAL, name TEXT, age INT);`  
- `INSERT INTO users VALUES (1, '민준', 25);`  
- `SELECT * FROM users;`

이런 식으로 DDL → DML 순으로 연습하면 데이터 흐름이 자연스럽게 이해된다.
