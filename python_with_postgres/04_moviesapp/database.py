import datetime
import sqlite3
from sqlite3.dbapi2 import Cursor

connection = sqlite3.connect("data.db")

# DDLs
DB_CREATE_MOVIES = "CREATE TABLE IF NOT EXISTS movies (id INTEGER PRIMARY KEY,title TEXT, release_timestamp REAL);"
DB_CREATE_USERS = "CREATE TABLE IF NOT EXISTS users (id INTEGER, username TEXT)"
DB_CREATE_WATCHED = """
CREATE TABLE IF NOT EXISTS watched (
    users_username TEXT,
    movie_id INTEGER,
    FOREIGN KEY (users_username) REFERENCES users(username),
    FOREIGN KEY (movie_id) REFERENCES movies(id));
"""

# mutations
DB_ADD_MOVIE = "INSERT INTO movies (title, release_timestamp) VALUES (?,?);"
DB_ADD_USER = "INSERT INTO users (username) VALUES (?)"
DB_ADD_WATCHED = "INSERT INTO watched (users_username, movie_id) VALUES (?,?);"
DB_DELETE_MOVIE = "DELETE FROM movies WHERE title = ?;"


# Queries
DB_GET_ALL_MOVIES = "SELECT id, title, release_timestamp FROM movies;"
DB_GET_UPCOMING_MOVIES = (
    "SELECT title, release_timestamp, watched FROM movies WHERE release_timestamp > ?;"
)
DB_GET_WATCHED_MOVIES = "SELECT * FROM watched WHERE users_username = ?;"


def create_schema():
    with connection:
        connection.execute(DB_CREATE_MOVIES)
        connection.execute(DB_CREATE_USERS)
        connection.execute(DB_CREATE_WATCHED)


def add_user(username):
    with connection:
        connection.execute(DB_ADD_USER, (username,))


def add_movie(title, release_timestamp):
    with connection:
        connection.execute(DB_ADD_MOVIE, (title, release_timestamp))


def get_movies(upcoming=False):
    with connection:
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
        connection.execute(DB_ADD_WATCHED, (username, movie_id))


def get_watched_movies(username):
    with connection:
        cursor = connection.cursor()
        cursor.execute(DB_GET_WATCHED_MOVIES, (username,))
        return cursor.fetchall()
