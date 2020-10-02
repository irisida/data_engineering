import datetime
import database

database.create_schema()


def prompt_add_movie():
    title = input("Movie Title: ")
    release_date = input("Release date (dd-mm-yyyy) : ")
    parsed = datetime.datetime.strptime(release_date, "%d-%m-%Y")
    timestamp = parsed.timestamp()
    database.add_movie(title, timestamp)


menu = """
1) Add new movie
2) View upcoming movies
3) View all movies
4) Watch a movie
5) See watched list

x) Exit

=> """


while (user_input := input(menu)) != "x":
    if user_input == "1":
        prompt_add_movie()
    if user_input == "2":
        pass
    if user_input == "3":
        pass
    if user_input == "4":
        pass
    if user_input == "5":
        pass
    else:
        print("Invaid input. Please try again.")
