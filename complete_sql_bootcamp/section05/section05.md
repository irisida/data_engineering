# SQL Deep dive

## SQL Terminology
- DCL (Data Control language)
    - GRANT
    - REVOKE
- DQL (Data Query Language)
    - SELECT
- DDL (Data Definition Language)
    - CREATE
    - ALTER
    - DROP
    - RENAME
    - TRUNCATE
    - COMMENT
- DML (Data Manipulation Language)
    - INSERT
    - UPDATE
    - DELETE
    - MERGE
    - CALL
    - EXPLAIN PLAN
    - LOCK TABLE

### DQL Notes
- concatenating columns with the `concat` function, taking in comma separated parameters.
- function types:
    - aggregate: aggregate data and produce one value, sums, avg etc...
    - scalar: run against each row (multiple outputs)
    - Importance of filtering with `WHERE`, `AND` and `OR`

### Sample queries

```sql
-- use the and filter option
select * from employees
where first_name = 'Mayumi'
and last_name = 'Schueller'
```

```sql
-- demonstrate the linked tables
select * from employees, salaries
where salaries.emp_no = employees.emp_no
and employees.emp_no = 10001
```

```sql
-- demonstrate conditional filtering
select * from customers
where gender = 'F'
AND (state = 'NY' OR state = 'OR')
```

```sql
-- using not to negate conditionals
select * from customers
where gender = 'F'
AND not (state = 'NY' OR state = 'OR')
```

```sql
-- demonstrates conditions an using `in` statement
select * from customers
where (age < 30 OR age >= 50)
AND income > 50000
and country IN ('Japan', 'Australia')
```

### Null values and null coalescing