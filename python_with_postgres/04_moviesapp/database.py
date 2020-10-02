import datetime
import sqlite3
from sqlite3.dbapi2 import Cursor

connection = sqlite3.connect("data.db")

# DDLs
DB_CREATE_MOVIES = (
    "CREATE TABLE IF NOT EXISTS movies (title TEXT, release_timestamp REAL);"
)
DB_CREATE_WATCHED = "CREATE TABLE IF NOT EXISTS watched (viewer TEXT, title TEXT);"

# mutations
DB_ADD_MOVIE = "INSERT INTO movies (title, release_timestamp) VALUES (?,?);"
DB_ADD_WATCHED = "INSERT INTO watched (viewer, title) VALUES (?,?);"
DB_DELETE_MOVIE = "DELETE FROM movies WHERE title = ?;"


# Queries
DB_GET_ALL_MOVIES = "SELECT title, release_timestamp FROM movies;"
DB_GET_UPCOMING_MOVIES = (
    "SELECT title, release_timestamp, watched FROM movies WHERE release_timestamp > ?;"
)
DB_GET_WATCHED_MOVIES = "SELECT * FROM watched WHERE viewer = ?;"


def create_schema():
    with connection:
        connection.execute(DB_CREATE_MOVIES)
        connection.execute(DB_CREATE_WATCHED)


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


def watch_movie(viewer, title):
    with connection:
        connection.execute(DB_DELETE_MOVIE, (title,))
        connection.execute(DB_ADD_WATCHED, (viewer, title))


def get_watched_movies():
    with connection:
        cursor = connection.cursor()
        cursor.execute(DB_GET_WATCHED_MOVIES)
        return cursor.fetchall()
