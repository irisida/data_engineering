import datetime
import database

database.create_schema()


def prompt_add_movie():
    title = input("Movie Title: ")
    release_date = input("Release date (dd-mm-yyyy) : ")
    parsed = datetime.datetime.strptime(release_date, "%d-%m-%Y")
    timestamp = parsed.timestamp()
    database.add_movie(title, timestamp)


def prompt_watched_movie():
    viewer = input("username: ")
    title = input("Movie title: ")
    database.watch_movie(viewer, title)


def print_movies_list(header, movies):
    print(f"-- Showing {header} movies --")
    for movie in movies:
        rel_date = datetime.datetime.fromtimestamp(movie[1])
        parsed_date = rel_date.strftime("%d-%b-%Y")
        print(f"Released: {parsed_date} Title: {movie[0]}")
    print("")


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

    elif user_input == "2":
        movies = database.get_movies(True)
        print_movies_list("upcoming", movies)

    elif user_input == "3":
        movies = database.get_movies()
        print_movies_list("ALL", movies)

    elif user_input == "4":
        prompt_watched_movie()

    elif user_input == "5":
        pass

    else:
        print("Invaid input. Please try again.")
