# 관계형 데이터베이스(Relational Database)
    데이터 간에 관계가 있는 데이터 항목들의 모음
- 테이블, 행, 열의 정보를 구조화하는 방식
- 서로 관련된 데이터 포인트를 저장하고 이에 대한 엑세스 제공

## 관계
    여러 테이블 간의 (논리적)연결

## 관계로 인해 할 수 있는 것
- 두 테이블을 사용하여 데이터를 다양한 형식으로 조회할 수 잇음


## 관계형 데이터베이스 용어
1. Table (aka Relation)​
- 데이터를 기록하는 곳, 관계라고도 불림
- table != DB
2. Field (aka Column, Attribute)​
- 열, 각 필드에는 고유한 데이터 형식(타입)이 지정됨
3. Record (aka Row, Tuple)​
- 행, 각 레코드에는 구체적인 데이터 값이 저장됨
4. Database (aka Schema)
- 테이블의 집합(데이터들의 모음), 스키마라고도 불림
5. Primary Key(PK)
- 각 레코드의 고유한 값
- 관계형 데이터베이스에서 레코드의 식별자(중복이 있으면 안됨, 고유한 값)로 활용
6. Foreign Key(FK)
- 테이블의 필드 중 다른 테이블의 레코드를 식별할 수 있는 키
- 각 레코드에서 서로 다은 테이블 간의 관계를 만드는 데 사용
- 관계형 데이터베이스의 핵심

## DBMS(Database management System)
    데이터베이스를 관리하는 소프트웨어 프로그램
    - RDBMS(Relational Database management System)
        - 관계형 데이터베이스를 관리하는 소프트웨어 프로그램
- 데이터 저장 및 관리를 용이하게 하는 시스템
- 데이터베이스와 사용자 간의 인터페이스 역할
    - 사용자가 데이터 구성, 업데이트, 모니터링, 백업, 복구 등을 할 수 있도록 도움

### 대표적인 RDMBS
- MySQL
- PostgreSQL
- Oracle Database
- MS SQL Server
- ...

### MySQL 구조
- Table < Database < Database Server(MySQL)

## 정리
- Table은 데이터를 기록하는 최종 위치
- 모든 Table에는 행에서 고유하게 식별 가능한 기본 키(PK)라는 속성이 있고, 외래 키(FK)를 사용하여 각 행에서 서로 다른 테이블 간의 관계를 만들 수 있음
- 데이터는 PK 또는 FK를 통해 결합(join)될 수 있는 여러 테이블에 걸쳐 구조화 됨
- MySQL은 이러한 Database들을 그룹핑하여 관련된 작업을 수행하는 Database Server