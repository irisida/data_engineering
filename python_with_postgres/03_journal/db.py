import sqlite3

connection = sqlite3.connect("data.db")


def create_tables():
    with connection:
        connection.execute(
            "CREATE TABLE IF NOT EXISTS entries (content TEXT, date TEXT);"
        )


def add_entry(content, entry_date):
    with connection:
        connection.execute("INSERT INTO entries VALUES(?,?);", (content, entry_date))


def get_entries():
    cursor = connection.execute("SELECT content, date FROM entries;")
    return cursor
