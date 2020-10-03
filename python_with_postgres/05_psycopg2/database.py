import os
import datetime
import psycopg2

from dotenv import load_dotenv

load_dotenv()


# DDLs
DB_CREATE_MOVIES = """
CREATE TABLE IF NOT EXISTS movies (
    id SERIAL PRIMARY KEY,
    title TEXT,
    release_timestamp REAL);
"""
DB_CREATE_USERS = "CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY);"
DB_CREATE_WATCHED = """
CREATE TABLE IF NOT EXISTS watched (
    users_username TEXT,
    movie_id INTEGER,
    FOREIGN KEY (users_username) REFERENCES users(username),
    FOREIGN KEY (movie_id) REFERENCES movies(id));
"""

# indexes
DB_CREATE_MOVIES_INDEX = (
    "CREATE INDEX IF NOT EXISTS idx_movies_release ON movies (release_timestamp);"
)


# mutations
DB_ADD_MOVIE = "INSERT INTO movies (title, release_timestamp) VALUES (%s,%s);"
DB_ADD_USER = "INSERT INTO users (username) VALUES (%s)"
DB_ADD_WATCHED = "INSERT INTO watched (users_username, movie_id) VALUES (%s,%s);"
DB_DELETE_MOVIE = "DELETE FROM movies WHERE title = %s;"


# Queries
DB_SEARCH_MOVIES = "SELECT id, title, release_timestamp FROM movies where title LIKE %s"

DB_GET_ALL_MOVIES = "SELECT id, title, release_timestamp FROM movies;"
DB_GET_UPCOMING_MOVIES = """
SELECT id, title, release_timestamp
FROM movies WHERE release_timestamp > %s;
"""
DB_GET_WATCHED_MOVIES = """
SELECT movies.*
FROM movies
JOIN watched on movies.id = watched.movie_id
JOIN users on users.username = watched.users_username
WHERE users.username = (%s);
"""

# Create the connection from the dictionary of the environment. This
# requires the os module we imported above. This process deoends upon
# the successful loading of the .env file that was called at the top
# and is part of the python-dotenv library.
connection = psycopg2.connect(os.environ["DATABASE_URL"])


def create_schema():
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(DB_CREATE_MOVIES)
            cursor.execute(DB_CREATE_USERS)
            cursor.execute(DB_CREATE_WATCHED)


def add_user(username):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(DB_ADD_USER, (username,))


def add_movie(title, release_timestamp):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(DB_ADD_MOVIE, (title, release_timestamp))


def get_movies(upcoming=False):
    with connection:
        with connection.cursor() as cursor:
            cursor = connection.cursor()
            if upcoming:
                # trigger the fetch of movies
                # with a timestamp that is
                # greater than right now.
                now_timestamp = datetime.datetime.today().timestamp()
                cursor.execute(DB_GET_UPCOMING_MOVIES, (now_timestamp,))
            else:
                cursor.execute(DB_GET_ALL_MOVIES)
            return cursor.fetchall()


def watch_movie(username, movie_id):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(DB_ADD_WATCHED, (username, movie_id))


def get_watched_movies(username):
    with connection:
        with connection.cursor() as cursor:
            cursor = connection.cursor()
            cursor.execute(DB_GET_WATCHED_MOVIES, (username,))
            return cursor.fetchall()


def search_movies(search_term):
    with connection:
        with connection.cursor() as cursor:
            cursor = connection.cursor()
            cursor.execute(DB_SEARCH_MOVIES, (f"%{search_term}%",))
            return cursor.fetchall()
