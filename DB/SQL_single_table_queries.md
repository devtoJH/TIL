# DQL(Data Query Language)

# 1. Querying data

## SELECT statement
    테이블에서 데이터를 조회

### SELECT syntax
```
SELECT
    select_list
FROM
    table_name;
```
- SELECT 키워드 다음에 데이터를 선택하려는 **필드를 하나 이상** 지정
- FROM 키워드 다음에 데이터를 선택하려는 **테이블의 이름**을 지정

### SELECT 예시
1. 테이블 employees에서 lastName 필드의 모든 데이터 조회
```
SELECT
    lastName
FROM
    employees;
```

2. 테이블 employees에서 lastName, firstName 필드의 모든 데이터를 조회
```
SELECT
    lastName, firstName
FROM
    employees;
```

3. 테이블 employees에서 모든 데이터를 조회
```
SELECT
    *
FROM
    employees;
```

4. 테이블 employees에서 firstName 필드의 모든 데이터를 조회
    - 단, 조회 시 firstName이 아닌 '이름'으로 출력될 수 있도록 출력명 변경
    - AS(alias) keyword : 필드에 새로운 별칭을 지정
```
SELECT
    firstName AS '이름'
FROM
    employees;
```

5. 테이블 orderdetails에서 productCode, 주문 총액 필드의 모든 데이터를 조회
    - 단, 주문 총액 필드는 quantityOrdered와 priceEach 필드를 곱한 값
    - Arithmetic Operators 기본적인 사칙연산 사용 가능
```
SELECT
    productCode,
    quantityOrdered * priceEach AS '주문 총액'
FROM
    orderdetails;
```

### SELECT 정리
- SELECT 문을 사용하여 테이블의 데이터를 조회 및 반환
- SELECT *(asterisk)를 사용하여 테이블의 모든 필드 선택

# 2. Sorting data

## ORDER BY clause
    조회 결과의 레코드를 정렬

### ORDER BY syntax
```
SELECT
    select_list
FROM
    table_name
ORDER BY
    column1 ASC 또는 DESC,
    column2 ASC 또는 DESC,
    ...;
```
- FROM clause 뒤에 위치
- 하나 이상의 컬럼을 기준으로 결과를 오름차순, 내림차순으로 정렬할 수 있음
    - ASC : 오름차순(기본 값) -> 생략 가능
    - DESC : 내림차순 -> 생략 불가능

### ORDER BY 예시
1. 테이블 employees에서 firstName 필드의 모든 데이터를 오름차순으로 조회
```
SELECT
    firstName
FROM
    employees
ORDER BY
    firstName;
```

2. 테이블 employees에서 firstName 필드의 모든 데이터를 내림차순으로 조회
```
SELECT
    firstName
FROM
    employees
ORDER BY
    firstName DESC;
```

3. 테이블 employees에서 lastName 필드를 기준으로 내림차순으로 정렬한 다음,
firstName 필드 기준으로 오름차순 정렬하여 조회
```
SELECT
    lastName, firstName
FROM
    employees
ORDER BY
    lastName DESC,
    firstName;
```

4. 테이블 orderdetails에서 totalSales 필드를 기준으로 내림차순으로 정렬한 다음,
productCode, totalSales 필드의 모든 데이터를 조회
    - 단, totalSales 필드는 quantityOrdered와 priceEach 필드를 곱한 결과 값
```
SELECT
    productCode,
    quantityOrdered * priceEach AS 'totalSales'
FROM
    orderdetails
ORDER BY
    totalSales DESC;
```

## SELECT statement 실행 순서
- FROM -> SELECT -> ORDER BY
    1. 테이블에서 (FROM)
    2. 조회하여 (SELECT)
    3. 정렬 (ORDER BY)

# 3. Filtering data
    데이터를 필터링하여 중복 제거, 조건 설정 등 SQL Query를 제어한다.

## Filtering data 관련 keywords
- Clause
    - DISTINCT
    - WHERE
    - LIMIT
- Operator
    - BETWEEN
    - IN
    - LIKE
    - Comparison
    - Logical

## DISTINCT clause
    조회 결과에서 중복된 레코드를 제거

### DISTINCT syntax
```
SELECT DISTINCT
    select_list
FROM
    table_name;
```
- SELECT 키워드 바로 뒤에 작성해야 함
- SELECT DISTINCT 키워드 다음에 고유한 값을 선택하려는 하나 이상의 필드를 지정

### DISTINCT 예시
1. 테이블 employees에서 lastName 필드의 모든 데이터를 오름차순으로 조회
```
SELECT
    lastName
FROM
    employees
ORDER BY
    lastName;
```

2. 테이블 employees에서 lastName 필드의 모든 데이터를 중복없이 오름차순으로 조회
```
SELECT DISTINCT
    lastName
FROM
    employees
ORDER BY
    lastName;
```

## WHERE clause
    조회 시 특정 검색 조건을 지정

### WHERE syntax
```
SELECT
    select_list
FROM
    table_name
WHERE
    search_condition;
```
- FROM clause 뒤에 위치
- search_condition은 비교연산자 및 논리연산자(AND, OR, NOT 등)를 사용하는 구문이 사용됨

### WHERE 예시
1. 테이블 employees에서 officeCode 필드 값이 1인 데이터의 lastName, firstName, officeCode 조회
```
SELECT
    lastName, firstName, officeCode
FROM
    employees
WHERE
    officeCode = 1;
```

2. 테이블 employees에서 jobTitle 필드 값이 'Sales Rep'이 아닌 데이터의 lastName, firstName, jobTitle 조회
```
SELECT
    lastName, firstName, jobTitle
FROM
    employees
WHERE
    jobTitle != 'Sales Rep';
```

3. 테이블 employees에서 officeCode 필드 값이 3 이상이고 jobTitle 필드 값이 'Sales Rep'인 데이터의 lastName, firstName, officeCode, jobTitle 조회
```
SELECT
    lastName, firstName, officeCode, jobTitle
FROM
    employees
WHERE
    officeCode >= 3 
    AND jobTitle = 'Sales Rep';
```

4. 테이블 employees에서 officeCode 필드 값이 5 미만이거나 jobTitle 필드 값이 'Sales Rep'이 아닌 데이터의 lastName, firstName, officeCode, jobTitle 조회
```
SELECT
    lastName, firstName, officeCode, jobTitle
FROM
    employees
WHERE
    officeCode < 5  
    OR jobTitle != 'Sales Rep';
```

5. 테이블 employees에서 officeCode 필드 값이 1에서 4 사이 값인 데이터의 lastName, firstName, officeCode 조회(1과 4를 포함)
```
SELECT
    lastName, firstName, officeCode
FROM
    employees
WHERE
    officeCode BETWEEN 1 AND 4;
========================================
WHERE
    officeCode >= 1
    AND officeCode <= 4;   -- 위의 WHERE절과 동일한 코드
```

6. 테이블 employees에서 officeCode 필드 값이 1에서 4 사이 값인 데이터의 lastName, firstName, officeCode를 오름차순 조회(1과 4를 포함)
```
SELECT
    lastName, firstName, officeCode
FROM
    employees
WHERE
    officeCode BETWEEN 1 AND 4
ORDER BY
    officeCode;
```

7. 테이블 employees에서 officeCode 필드 값이 1 또는 3 또는 4 값인 데이터의 lastName, firstName, officeCode를 조회
```
SELECT
    lastName, firstName, officeCode
FROM
    employees
WHERE
    officeCode IN (1, 3, 4);
========================================
WHERE
    officeCode = 1
    OR officeCode = 3
    OR officeCode = 4;   -- 위의 WHERE절과 동일한 코드
```

8. 테이블 employees에서 officeCode 필드 값이 1과 3 그리고 4가 아닌 데이터의 lastName, firstName, officeCode를 조회
```
SELECT
    lastName, firstName, officeCode
FROM
    employees
WHERE
    officeCode NOT IN (1, 3, 4);
```

9. 테이블 employees에서 lastName 필드 값이 son으로 끝나는 데이터의 lastName, firstName 조회
```
SELECT
    lastName, firstName
FROM
    employees
WHERE
    lastName LIKE '%son';
```

10. 테이블 employees에서 firstName 필드 값이 4자리면서 y로 끝나는 데이터의 lastName, firstName 조회
```
SELECT
    lastName, firstName
FROM
    employees
WHERE
    lastName LIKE '___y';
```

### Comparison Operators
- 비교 연산자
    - =, >=, <=, IS, LIKE, IN, BETWEEN, ...
    - IN : 값이 특정 목록 안에 있는지 확인
    - LIKE : 값이 특정 패턴에 일치하는지 확인 with Wildcards
    - Wildcards
        - % : **0개 이상의 문자열**과 일치하는지 확인
        - _ : **단일 문자**와 일치하는지 확인

### Logical Operators
- 논리 연산자
    - AND(&&), OR(||), NOT(!)

## LIMIT clause
    조회하는 레코드 수를 제한
```
SELECT
    select_list
FROM
    table_name
LIMIT [offset,] row_count;
```
- LIMIT clause는 하나 또는 두 개의 인자를 사용(0 또는 양의 정수)
- row_count는 조회할 최대 레코드 수를 지정

### LIMIT & OFFSET 예시
```
SELECT
    ...
FROM
    ...
LIMIT 3, 5;
===============
1
2
3
4 <= OFFSET 3
5
6
7
8 <= ROW_COUNT 5
```

1. 테이블 customers에서 contactFirstName, creditLimit 필드 데이터를 creditLimit 기준 내림차순으로 7개만 조회
```
SELECT
    contactFirstName, creditLimit
FROM
    customers
ORDER BY
    creditLimit DESC
LIMIT 7;
```

2. 테이블 customers에서 contactFirstName, creditLimit 필드 데이터를 creditLimit 기준 내림차순으로 4번째부터 7번째 데이터만 조회
```
SELECT
    contactFirstName, creditLimit
FROM
    customers
ORDER BY
    creditLimit DESC
LIMIT 3, 4;
============================
LIMIT 3 OFFSET 4;  -- 위의 LIMIT절과 동일한 코드
```

# 4. Grouping data

## GROUP BY clause
    레코드를 그룹화하여 요약본 생성 with 집계 함수(Aggregation Function)

## Aggregation Function
    값에 대한 계산을 수행하고 단일한 값을 반환하는 함수
    - SUM, AVG, MAX, MIN, COUNT

### GROUP BY syntax
```
SELECT
    c1, c2, ..., cn, aggregate_function(ci)
FROM
    table_name
GROUP BY
    c1, c2, ..., cn;
```
- FROM 및 WHERE 절 뒤에 배치
- GROUP BY 절 뒤에 그룹화할 필드 목록을 작성

### GROUP BY 이해하기
1. jobTitle 필드를 그룹화
```
SELECT
    jobTitle
FROM
    employees
GROUP BY
    jobTitle;
```

| jobTitle |
|:---:|
| President |
| VP Sales |
| VP Marketing |
| Sales Manager (APAC) |
| Sales Manager (EMEA) |
| Sales Manager (NA) |
| Sales Rep |

2. COUNT 함수가 각 그룹에 대한 집계된 값을 계산
```
SELECT
    jobTitle, COUNT(*)
FROM
    employees
GROUP BY
    jobTitle;
```

| jobTitle | COUNT(*) |
|:---:|:---:|
| President | 1 |
| VP Sales | 1 |
| VP Marketing | 1 |
| Sales Manager (APAC) | 1 |
| Sales Manager (EMEA) | 1 |
| Sales Manager (NA) | 1 |
| Sales Rep | 17 |

### GROUP BY 예시
1. 테이블 costomers에서 country 필드를 그룹화하여 각 그룹에 대한 creditLimit의 평균값을 내림차순 조회
```
SELECT
    country, AVG(creditLimit)
FROM
    costomers
GROUP BY
    country
ORDER BY
    AVG(creditLimit) DESC;
```

2. 테이블 costomers에서 country 필드를 그룹화하여 각 그룹에 대한 creditLimit의 평균값이 80000을 초과하는 데이터만 조회
```
SELECT
    country, AVG(creditLimit)
FROM
    costomers
WHERE
    AVG(creditLimit) > 80000
GROUP BY
    country;

-- 에러 발생 : Invalid use of group function
```

- HAVING clause : 집계 항목에 대한 세부 조건을 지정
    - GROUP BY와 함께 사용되며, GROUP BY가 없다면 WHERE 사용
```
SELECT
    country, AVG(creditLimit)
FROM
    costomers
GROUP BY
    country
HAVING
    AVG(creditLimit) > 80000;
```

## SELECT statment 실행 순서
- FROM -> WHERE -> GROUP BY -> HAVING -> SELECT -> ORDER BY -> LIMIT
    1. 테이블에서(FROM)
    2. 특정 조건에 맞춰(WHERE)
    3. 그룹화 하고(GROUP BY)
    4. 만약 그룹 중에서 조건이 있다면 맞추고(HAVING)
    5. 조회하여(SELECT)
    6. 정렬하고(ORDER BY)
    7. 특정 위치의 값을 가져온다.(LIMIT)

## 참고
### 정렬에서의 NULL
- MY SQL에서 NULL은 NULL이 아닌 값 앞에 위치
    - NULL 값이 존재할 경우 오름차순 정렬 시 결과에 NULL이 먼저 출력
```
-- NULL 정렬 예시
SELECT
    postalCode
FROM
    customers
ORDER BY
    postalCode;
```
