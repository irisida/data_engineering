# Database & SQL fundamentals

## What is SQL?
- SQL is a language that is used to talk to the database in a way the database engine can understand.
- SQL is also a standard and a way to deliver concepts in a familiar format that does not require learning an entire language and implementation per database engine.
- Structured query language means exactly that, Structured! It is a formatted way to ask the database about the data it stores, to retrieve and show specific subsets of the data.
- Statements we interact with the database with are typically for the reading, creating, updating or deletion of data. This is known as CRUD, or CRUD operations. SQL allows us to phrase our CRUD operations in a standard way that is English-like in its syntax.

## What is a Query?
- A query is simply an instruction or statement.
- It is a CRUD directive issued to the database.

## SQL is a Declarative language
SQL is a declarative language, this means we declare what will happen, not how. Where we specify how an action will happen is where we are using imprerative languages.

## SQL history - SQL Vs SEQUEL
- A product of the later 1970, formalised in the 1980's. See paper [here](https://www.seas.upenn.edu/~zives/03f/cis550/codd.pdf)
- 1st edition was created by other IBM developers implementing Codds paper.
- Before databases were file processing systems, data saved to individual files. No relationships were established.

## Database models
- Hierarchical
    - parent/child structure.
    - Tightly coupled.
    - One-to-many relationship.
- Netowrking
    - Extension of hierarchical that allows many-to-many relationships.
- Entity-Relationship
- Relational
    - unique identifier driven
    - relational tables
    - normalising data
- Object-Oriented
- Flat
- Semi-Structured

## Relational model terms
- Schema
- Attribute
- Cardinality
- Tuple
- Column
- Key
- Table
- Primary & foreign keys

## OLTP vs OLAP
- OLTP - online transaction processing, this is the day to day business database. (users orders purchases)
- OLAP - online analytical processing, insights, warehoused, deriving MI/BI from the data.
