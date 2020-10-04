# Python with postgres SQL


[course link](https://www.udemy.com/course/complete-python-postgresql-database-course)

- section 1 - Introduction - _skipped_
- section 2 - Python refresher - _skipped_
- section 3 - Journal project with SQLite
- section 4 - Movie watchlist app with SQLite
- section 5 - Intro to postgres and migrating an app
- section 6 - Building a poll app
- section 7 - dates and times
- section 8 - advanced postgres features
- section 9 - charting with matplotlib


# Theory Notes

- **ACID** - **A**tomicity, **C**onsistency, **I**solation & **D**urability. This is an approach that is supported or delivered by the concept of transactions. The atomocity comes from all operations in a transaction being indivisible, either they all succeed, or none do. With consistency, it means the rules of the database are followed at all times. By example, no foreign key pointing to a non-existent primary key. We achieve isolation by only having the data available,, or visible in the database once the trnsaction has completed and committed successfully. DUrability means the data is saved to a permanent storage once a transaction is committed.
- In memory Database - faster, but volatile and will lose work/state in a crash.


# SQL Notes
- Within SQL statements in postgres we can use the `RETURNING` keyword to negate the need for follow up queries in a transaction to see rows that are inserted or updated.
- Use of nested queries should avoid a semi-colon on the inner query to avoid undesired side effects.
- Nested queries can be used as:
    - Anywhere a colum, table or dataset is referenced
    - columns of a SELECT
    - Values of an INSERT
    - VALUE of a WHERE
- You can use the WITH to extract subqueries and lower the cognitive load of complex SQL.
```SQL
WITH latest_id as (
    SELECT id FROM polls ORDER BY id DESC LIMIT 1
)

SELECT * FROM polls
JOIN options ON polls.id = options.poll_id
WHERE polls.id = (SELECT * FROM latest_id);
```
-