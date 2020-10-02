import datetime
import sqlite3
from sqlite3.dbapi2 import Cursor

connection = sqlite3.connect("data.db")


DB_CREATE_SCHEMA = """CREATE TABLE IF NOT EXISTS movies (
    title TEXT,
    release_timestamp REAL,
    watched INTEGER
);"""

DB_ADD_MOVIE = "INSERT INTO movies (title, release_timestamp, watched) VALUES (?,?,0);"

DB_GET_ALL_MOVIES = "SELECT title, release_timestamp, watched FROM movies;"

DB_GET_UPCOMING_MOVIES = (
    "SELECT title, release_timestamp, watched FROM movies WHERE release_timestamp > ?;"
)

DB_GET_WATCHED_MOVIES = (
    "SELECT title, release_timestamp, watched FROM movies WHERE watched = 1;"
)

DB_SET_MOVIE_AS_WATCHED = "UPDATE movies SET watched = 1 WHERE title = ?;"


def create_schema():
    with connection:
        connection.execute(DB_CREATE_SCHEMA)


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


def watch_movie(title):
    with connection:
        connection.execute(DB_SET_MOVIE_AS_WATCHED, (title,))


def get_watched_movies():
    with connection:
        cursor = connection.cursor()
        cursor.execute(DB_GET_WATCHED_MOVIES)
        return cursor.fetchall()
