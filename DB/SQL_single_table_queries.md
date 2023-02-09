# Querying data

## SELECT statement
    테이블에서 데이터를 조회

### SELECT syntax
```Database
SELECT
    select_list
FROM
    table_name;
```
- SELECT 키워드 다음에 데이터를 선택하려는 **필드를 하나 이상** 지정
- FROM 키워드 다음에 데이터를 선택하려는 **테이블의 이름**을 지정

### SELECT 예시
1. 테이블 employees에서 lastName 필드의 모든 데이터 조회
```Database
SELECT
    lastName
FROM
    employees;
```

2. 테이블 employees에서 lastName, firstName 필드의 모든 데이터를 조회
```Database
SELECT
    lastName, firstName
FROM
    employees;
```

3. 테이블 employees에서 모든 데이터를 조회
```Database
SELECT
    *
FROM
    employees;
```

4. 테이블 employees에서 firstName 필드의 모든 데이터를 조회
    - 단, 조회 시 firstName이 아닌 '이름'으로 출력될 수 있도록 출력명 변경
    - AS(alias) keyword : 필드에 새로운 별칭을 지정
```Database
SELECT
    firstName AS '이름'
FROM
    employees;
```

5. 테이블 orderdetails에서 productCode, 주문 총액 필드의 모든 데이터를 조회
    - 단, 주문 총액 필드는 quantityOrdered와 priceEach 필드를 곱한 값
    - Arithmetic Operators 기본적인 사칙연산 사용 가능
```Database
SELECT
    productCode,
    quantityOrdered * priceEach AS '주문 총액'
FROM
    orderdetails;
```

### SELECT 정리
- SELECT 문을 사용하여 테이블의 데이터를 조회 및 반환
- SELECT *(asterisk)를 사용하여 테이블의 모든 필드 선택

# Sorting data

## ORDER BY clause
    조회 결과의 레코드를 정렬

### ORDER BY syntax
```Database
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
```Database
SELECT
    firstName
FROM
    employees
ORDER BY
    firstName;
```

2. 테이블 employees에서 firstName 필드의 모든 데이터를 내림차순으로 조회
```Database
SELECT
    firstName
FROM
    employees
ORDER BY
    firstName DESC;
```

3. 테이블 employees에서 lastName 필드를 기준으로 내림차순으로 정렬한 다음,
firstName 필드 기준으로 오름차순 정렬하여 조회
```Database
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
```Database
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