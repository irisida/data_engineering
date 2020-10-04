from typing import List, Tuple
from psycopg2.extras import execute_values

Poll = Tuple[int, str, str]
Vote = Tuple[str, int]
PollWithOption = Tuple[int, str, str, int, str, int]
PollResults = Tuple[int, str, int, float]


CREATE_POLLS = """CREATE TABLE IF NOT EXISTS polls
(id SERIAL PRIMARY KEY, title TEXT, owner_username TEXT);"""

CREATE_OPTIONS = """CREATE TABLE IF NOT EXISTS options
(id SERIAL PRIMARY KEY, option_text TEXT, poll_id INTEGER, FOREIGN KEY(poll_id) REFERENCES options (id));"""

CREATE_VOTES = """CREATE TABLE IF NOT EXISTS votes
(username TEXT, option_id INTEGER, FOREIGN KEY(option_id) REFERENCES options(id));"""


SELECT_ALL_POLLS = "SELECT * FROM polls;"
SELECT_POLL_WITH_OPTIONS = """SELECT * FROM polls
JOIN options ON polls.id = options.poll_id
WHERE polls.id = %s;"""
SELECT_LATEST_POLL = """
SELECT * FROM polls
JOIN options on polls.id = options.poll_id
WHERE polls.id = (
    SELECT id from polls ORDER BY id DESC LIMIT 1
)
"""
SELECT_POLL_VOTE_DETAILS = """
SELECT
  options.id,
  options.option_text,
  COUNT(votes.option_id) as vote_count,
  COUNT(votes.option_id) / SUM(COUNT(votes.option_id)) OVER() * 100.0 AS Percentage
FROM options
LEFT JOIN votes on options.id = votes.option_id
WHERE options.poll_id = %s
GROUP BY options.id
"""

SELECT_RANDOM_VOTE = (
    "SELECT * FROM votes WHERE option_id = %s ORDER BY RANDOM() LIMIT 1"
)

INSERT_POLL = "INSERT INTO polls (title, owner_username) VALUES (%s, %s) RETURNING id"
INSERT_OPTION = "INSERT INTO options (option_text, poll_id) VALUES %s;"
INSERT_VOTE = "INSERT INTO votes (username, option_id) VALUES (%s, %s);"


def create_tables(connection):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(CREATE_POLLS)
            cursor.execute(CREATE_OPTIONS)
            cursor.execute(CREATE_VOTES)


def get_polls(connection) -> List[Poll]:
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(SELECT_ALL_POLLS)
            return cursor.fetchall()


def get_latest_poll(connection) -> List[PollWithOption]:
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(SELECT_LATEST_POLL)
            return cursor.fetchall()


def get_poll_details(connection, poll_id: int) -> List[PollWithOption]:
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(SELECT_POLL_WITH_OPTIONS, (poll_id,))
            return cursor.fetchall()


def get_poll_and_vote_results(connection, poll_id: int) -> List[PollResults]:
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(SELECT_POLL_VOTE_DETAILS, (poll_id,))
            return cursor.fetchall()


def get_random_poll_vote(connection, option_id: int) -> Vote:
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(SELECT_RANDOM_VOTE, (option_id,))
            return cursor.fetchone()


# Makes use of the returning SQL keyword in order to passback the
# generated id for the new row in the insert query. To minimise the
# boilerplate code we also make use of the psycopg2.extra.execute_values
# function to iterate the insert over the options that were put into the
# list comprehension from the text and poll id related.
def create_poll(connection, title: str, owner: str, options: List[str]):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(INSERT_POLL, (title, owner))
            poll_id = cursor.fetchone()[0]
            option_values = [(option_text, poll_id) for option_text in options]
            execute_values(cursor, INSERT_OPTION, option_values)


def add_poll_vote(connection, username: str, option_id: int):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(INSERT_VOTE, (username, option_id))
