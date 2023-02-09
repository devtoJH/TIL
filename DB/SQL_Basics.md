# SQL(Structure Query Language)
    - 데이터베이스에 정보를 저장하고 처리하기 위한 프로그래밍 언어
    - Structure : 테이블의 형태로 구조화된 관계형 데이터베이스
    - Query : 테이블의 형태로 구조화된 관계형 데이터베이스에게 요청을 질의(요청)
        - 일반적으로 SQL로 작성하는 코드를 쿼리문(SQL문)이라 함
    - Language : 언어
- 컴퓨터와의 대화 -> 프로그래밍 언어
- 관계형 데이터베이스와의 대화 -> SQL

## SQL Sytax
    SELECT column_name FROM table_name;
- SQL 키워드는 대소문자를 구분하지 않는다.
    - 하지만 대문자로 작성하는 것을 권장(명시적 구분)
- 각 SQL Statements의 끝에는 세미콜론(;)이 반드시 필요
    - 각 문장들을 구분하기 위해서

## SQL Statements
    SQL 언어를 구성하는 가장 기본적인 코드 블록

### SQL Statements 예시
    SELECT column_name FROM table_name;
- 위의 문장에서 2개의 keyword가 있다.(SELECT, FROM)

## SQL Statements 유형
- 데이터베이스에서 수행 목적에 따라 대체로 4가지로 나뉜다.
    - DDL(Data Definition Language) : 데이터 정의
        - SQL 키워드 : CREATE, DROP, ALTER
    - DQL(Data Query Language) : 데이터 검색
        - SQL 키워드 : SELECT
    - DML(Data Manipulation Language) : 데이터 조작(추가, 수정, 삭제)
        - SQL 키워드 : INSERT, UPDATE, DELETE
    - DCL(Data Control Language) : 데이터 제어(사용자의 권한, 계정)
        - SQL 키워드 : COMMIT, ROLLBACK, GRANT, REVOKE