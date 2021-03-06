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

### Keywords
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
- Postgres has typical math functions bundled:
    - `RANDOM` for random value between 0.0 & 1.0
    - `abs(x)` to get the absolute value of x
    - `mod(y, x)` gives the remainder of y/x
    - loads more....


### Aggregation
- `count(expr)` is an aggregate function and takes an expression. So we typically pass a query to be evaluated (expression) and the count is the number of rows returned by evaluating that expression.
- `avg(expr)` return the average of the results returned by the expression.
- `max(expr)` & `min(expr)` give the max and min respectively.
- again, there are loads more in the documentation.
- group by rules:
    - You keep the coluns you groupded on, but reduced to single data points. losing access to other columns
    - aggregate functions on every column

### Window functions
- `OVER()` allows programmer to perform operations on columns featured in a group by as a whole. Effectively it is treated like a separate query and runs on a window of the data in operation. All other aggregators will run in a query run cycle before the OVER() is applied.
- `RANK()` rank added to the query would effectively be operating only upo the current row therefore requires the OVER() window to be created. With rank we require the column to base ranking on otherwise it will apply the base ranking to all and we will normally see each row have a ranking of 1.
- `DENSE_RANK()` the dense version doesn't skip a rank where a duplicate, multi-participant rank is achieved.
- in a multi-ranking situation we can use `PARTITION` and supply the column we want to divide rankings by.
- `DISTINCT ON` option to return the first of each grouped option.
- simple view - runs the underlying query to generate a table
- materialized view - does not re-run each time, is persisted and has to be called to refresh to update.