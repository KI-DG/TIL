# DAY01

## Database

- 데이터베이스 전엔 파일을 이용한 데이터 관리를 하였다

  - 이메일이나 메신저를 이용해 간편하게 전송 가능

  - 대용량 데이터를 다루기에 적합하지 않음

  - 구조적으로 정리하게에 어려움

- 스프레드 시트 이용한 데이터 관리
  - 컬럼(열)을 통해 데이터의 유형을 지정하고 레코드(행)을 통해 구체적인 데이터 값을 포함
  - ex) 엑셀
- 데이터 베이스 
  - 프로그래밍 언어를 사용해 작동 시킬 수 있음
  - RDB라고 부르는 관계형 데이터베이서
  - 각각의 데이터를 테이블에 기입함

### 정의

- 체계화된 데이터의 모임
- 여러사람이 공유하고 사용할 목적으로 통합 관리되는 정보의 집합
- 검색, 구조화 같은 작업을 보다 수비게 하기위해 조직화된 데이터를 수집하는 저장 시스템
  - 검색과 갱신의 효율화
- DBMS == Database를 조적하는 프로그램
  - Oracle, MySQL, SQLite 등이 모두 DMBS
- 관계형 데이터베이스 관리 시스템(RDBMS) 을 사용

#### RDB

- 관계형 데이터 베이스
- 기본구조
  1. 스키마
  2. 테이블
     - 필드 
     - 레코드
     - 기본 키(PK)

- 이점
  - 데이터를 직관적으로 표현할 수 있음
  - 관련한 각 데이터에 쉽게 접근할 수 있음
  - 대량의 데이터도 효율적으로 관리 가능
- SQLite
  - 비교적 가벼운 데이터베이스

#### SQL

- Structured Query Language
- 특수 목적의 프로그래밍 언어
- 스키마를 생성 및 수정할 수있으며, 테이블에서의 자료 검색 및 관리도 할 수 있음
- SQL을 표준으로 채택하고 있음
- 명령어
  - DDL
    - 데이터 정의 언어
    - 테이블, 스키마를 정의 하기 위한 명령어
  - DML
    - 데이터 조작 언어
    - 데이터를 조작하기 위한 명령어
  - DCL
- 들여쓰기는 중요하지 않고 세미콜론이 중요하다 
- 키우더는 대소문자를 구분하지 않지만 대문자를 작성하는 것을 권장 

#### DDL

- 테이블 구조를 관리
  - CREATE, ALTER, DROP

```sqlite
CREATE TABLE contacts(
  name(이름) TEXT(타입) NOT NULL(제약조건),
  age INTEGER NOT NULL,
  email TEXT NOT NULL UNIQUE
);
```

- Data Types

1. NULL
   - 정보가 없거나 알 수 없음을 의미
   - 값이 따옴표 없이 NULL일 때
2. INTEGER
   - 정수 
   - 크기에 따라 0, 1, 2, 3, 4, 6 또는 8 바이트와 같은 가변 크기를 가짐
   - 값에 둘러싸는 따옴표와 소수점 또는 지수가 없을때
3. REAL
   - 실수
   - 값에 따옴표나 소수점, 지수가 없을 때
4. TEXT
   - 문자 데이터
   - 값이 작은 따옴표나 큰따옴표로 묶일때
5. BLOB
   - 입력된 그래도 저장된 데이터 덩어리 (대용 타입 없음)
   - 바이너리 등 멀티미디어 파일

날짜와 시간의 타입은 따로 존재는 하지 않는다

- Binary Data
  - 데이터의 저장과 처리를 목적으로 0 과 1의 이진 형식으로 인코딩 된 파일

- SQLite Datatypes 특징

  - 컬럼에 저장된 값에 따라 데이터 타입이 결정됨
  - 정수 1을 넣을 경우 INTEGER로 타입이 지정 문자 '1'을 넣을 경우 TEXT 타입으로 지정
  - 동적 타입 시스템을 사용하면 기존의 엄격하게 타입이 지정된 데이터베이스에서는 불가능한 작업을 유연하게 수행할 수 있음
  - 정적 타입 시스템이 지정된 데이터베이스에서 작동하는 SQL 문이 SQLite에서 동일한 방식으로 작동
  - 데이터 타입을 지정하는 것을 권장

- Type Affinity

  - 타입선호도 

  1. INTEGER
  2. TEXT
  3. BLOB
  4. REAL
  5. NUMERIC

  - 선호도 존재 이유 - 호환성을 최대화 하기 위해 

- Constraints 종류

1. NOT NULL
   - 컬럼이 NULL 값을 허용하지 않도록 지정
2. UNIQUE
   - 컬럼의 모든 값이 서로 구별되거나 고유한 값이 되도록 함
3. PRIMARY KEY
   - 테이블에서 행의 고유성을 식별하는데 사용되는 컬럼
   - 각 테이블에서 하나의 기본 키만 있음
   - 암시적으로 NOT NULL 제약 조건이 포함되어 있음
4. AUTOINCREMENT
   - 사용되지 않은 값이나 이전에 삭제된 행의 값을 재사용하는 것을 방지
   - Django에서 테이블 생성 시 id 컬럼에 기본적으로 사용하는 제약조건

#### rowid

- 암시적 자동 증가 컬럼 자동으로 생성
- 고유하게 식별하는 64비트 부호 있는 정수 값
- 새 행을 삽입할 때마다 정수 값을 자동으로 할당
  - 값은 1에서 시작
  - 가장 큰 rowid 보다 하나 큰 다음 순차 정수를 자동으로 할당
- 컬럼을 직접 만들면 컬럼은 rowid 컬럼의 별칭이 됨

#### ALTER TABLE

- 기존 테이블의 구조를 수정

1. 테이블의 이름을 변경
2. 컬럼 이름을 변경
3. 새로운 컬럼을 추가 
4. 컬럼 삭제

```sqlite
ALTER TABLE contacts RENAME TO new_contacts;
-- 기존의 테이블 이름을 바꿔주는것 

ALTER TABLE new_contacts RENAME COLUMN name TO last_name;
-- 기존의 컬럼의 이름을 바꿔주는것

ALTER TABLE new_contacts ADD COLUMN address Text NOT NULL;
-- 컬럼을 추가 되는 것
-- 주의사항 테이블에 데이터가 있는경우
-- Cannot add NOT NULL column with default value NULL (오류발생)
-- 해결방법
-- ALTER TABLE new_contacts ADD COLUMN address Text NOT NULL DEFAULT 'no address';

ALTER TABLE new_contacts DROP COLUMN address;
-- 컬럼 삭제
-- 삭제하지 못하는경우 
-- 컬럼이 다른 부분에서 참조되는 경우
-- PRIMARY KEY 인경우
-- UNIQUE 제약조건이 있는 경우
```

#### DROP TABLE

- 기존 테이블 삭제

```sqlite
DROP TABLE new_contacts;
-- 테이블 삭제
-- 한 번에 하나의 테이블만 삭제 
-- 여러 테이블을 제거하려면 여러번 사용
-- 실행취소하거나 복구할 수 없음
```

#### DML

INSERT - Create

SELECT - Read

UPDATE - Update

DELETE - Delete

```sqlite
CREATE TABLE users(
  first_name TEXT NOT NULL,
  last_name TEXT NOT NULL,
  age INTEGER NOT NULL,
  country TEXT NOT NULL,
  phone TEXT NOT NULL,
  balance INTEGER NOT NULL
);
```

