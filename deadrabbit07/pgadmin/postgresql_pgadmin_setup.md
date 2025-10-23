# PostgreSQL 및 pgAdmin 초보자 설정 가이드 (도서 관리 시스템 프로젝트)

이 문서는 PostgreSQL과 pgAdmin이 설치되어 있음을 전제로 하며,  
프로젝트 환경 설정부터 기본적인 SQL 쿼리 실습까지의 과정을 담고 있습니다.

---

## 1. PostgreSQL 비밀번호 재설정 및 사용자/권한 확인 (Mac 기준)

pgAdmin 접속 오류 해결 및 비밀번호 재설정을 위해 실제 데이터베이스 사용자(Role)를 확인하고 비밀번호를 재설정합니다.

### 1.1. 현재 접속 사용자 확인

터미널에서 `psql`을 통해 실제 데이터베이스 관리자 사용자 이름을 확인합니다.

터미널을 열고 기본 DB에 접속합니다.

```bash
psql postgres
```

(성공 시 `postgres=#` 프롬프트가 뜹니다.)

현재 접속된 실제 사용자(Role) 이름을 확인합니다.

```sql
SELECT current_user;
```

(출력된 이름을 기억하세요. 예: `user`)

---

### 1.2. 비밀번호 재설정 및 적용

확인된 사용자 이름을 사용하여 새 비밀번호를 설정합니다.  
(예시: 사용자 이름은 `user`, 새 비밀번호는 `339911`로 설정)

```sql
ALTER USER "user" WITH PASSWORD '339911';
```

(성공 시 `ALTER ROLE` 메시지가 나타납니다.)

`psql`을 종료합니다.

```sql
\q
```

---

## 2. 새로운 데이터베이스 사용자 생성 (선택 사항)

새로운 프로젝트를 위해 별도의 사용자 계정을 만들고 싶을 때 사용합니다.

터미널에서 기본 DB에 관리자(`user`) 권한으로 재접속합니다.

```bash
psql -U user postgres
```

새로운 사용자(`new_project_user`)를 생성하고 비밀번호를 지정합니다.

```sql
CREATE USER new_project_user WITH PASSWORD '새로운비밀번호';
```

- `CREATE USER`: 새로운 데이터베이스 사용자(Role)를 만듭니다.  
- `WITH PASSWORD`: 해당 사용자의 비밀번호를 지정합니다.

`psql`을 종료합니다.

```sql
\q
```

---

## 3. pgAdmin 서버 연결 설정 수정

pgAdmin이 올바른 사용자 이름과 새 비밀번호를 사용하도록 연결 정보를 수정합니다.

1. **pgAdmin 접속 정보 수정**  
   - pgAdmin 왼쪽 탐색기에서 **Servers → [서버 이름]**을 마우스 오른쪽 버튼으로 클릭하고 **Properties**를 선택합니다.

2. **Connection 탭 수정**
   - `Username` 필드를 `postgres`에서 실제 사용자 이름(`user` 또는 `new_project_user`)으로 수정합니다.
   - `Password` 필드에 해당 사용자의 비밀번호를 입력합니다.

3. **Save**를 클릭하여 저장하고 서버에 재접속합니다.

---

## 4. 데이터베이스 및 테이블 생성 (도서 관리 시스템 구축)

### 4.1. 프로젝트 데이터베이스 생성 (pgAdmin)

1. 왼쪽 탐색기에서 **Servers → Databases** 폴더를 마우스 오른쪽 버튼으로 클릭 후  
   **Create → Database...** 를 선택합니다.
2. `Database` 필드에 `my_project_db` 를 입력합니다.
3. **Owner**가 `user` 또는 새로 만든 사용자임을 확인하고 **Save**를 클릭합니다.

---

### 4.2. 테이블 생성 및 데이터 입력 (터미널 psql)

`my_project_db` 에 접속합니다.

```bash
psql -U user my_project_db
```

(비밀번호 입력 후 `my_project_db=#` 프롬프트 확인)

#### authors (저자) 테이블 생성

```sql
CREATE TABLE authors (
    author_id SERIAL PRIMARY KEY,    -- 기본 키 (자동 증가, 유일값)
    name VARCHAR(100) NOT NULL,      -- 저자 이름 (필수 입력)
    nationality VARCHAR(50)
);
```

#### books (도서) 테이블 생성 (외래 키 포함)

```sql
CREATE TABLE books (
    book_id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    published_year INTEGER,
    author_id INTEGER REFERENCES authors(author_id)  -- 외래 키: authors 테이블과 연결
);
```

#### 데이터 입력 (순서 중요: 저자 → 도서)

```sql
-- 저자 입력
INSERT INTO authors (name, nationality) VALUES
    ('김영하', '대한민국'),
    ('무라카미 하루키', '일본'),
    ('J.K. 롤링', '영국');

-- 도서 입력 (author_id는 1, 2, 3으로 자동 부여됨)
INSERT INTO books (title, published_year, author_id) VALUES
    ('살인자의 기억법', 2013, 1),
    ('여행의 이유', 2019, 1),
    ('노르웨이의 숲', 1987, 2),
    ('해리 포터와 마법사의 돌', 1997, 3);
```

---

## 5. SQL 문법 학습 및 pgAdmin 시각화

### 5.1. 데이터 JOIN 실습 (터미널)

두 테이블을 연결하여 데이터를 조회하는 `INNER JOIN`을 실습합니다.

```sql
SELECT
    b.title AS 책_제목,
    a.name AS 저자_이름,
    b.published_year AS 출판_연도
FROM
    books b
INNER JOIN
    authors a ON b.author_id = a.author_id;
```

---

### 5.2. pgAdmin에서 테이블 새로고침 (Refresh)

터미널에서 SQL 명령을 실행한 후 pgAdmin에서 최신 정보를 반영하는 방법입니다.

1. pgAdmin 왼쪽 탐색기에서 **my_project_db → Schemas → public → Tables** 폴더를 찾습니다.  
2. `Tables` 폴더를 마우스 오른쪽 버튼으로 클릭합니다.  
3. 메뉴에서 **Refresh** 를 선택합니다.

---

### 5.3. 데이터 시각화 확인 (pgAdmin)

1. 새로고침된 `authors` 또는 `books` 테이블을 마우스 오른쪽 버튼으로 클릭 후  
   **View/Edit Data → All Rows** 를 선택하여 데이터를 표 형태로 확인합니다.

2. `my_project_db`에서 **Query Tool**을 열어 `JOIN` 쿼리를 붙여넣고 실행하여 결과를 시각적으로 확인합니다.

---
