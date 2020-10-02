import datetime
import database

database.create_schema()


def prompt_add_user():
    username = input("Enter new username: ")
    database.add_user(username)


def prompt_add_movie():
    title = input("Movie Title: ")
    release_date = input("Release date (dd-mm-yyyy) : ")
    parsed = datetime.datetime.strptime(release_date, "%d-%m-%Y")
    timestamp = parsed.timestamp()
    database.add_movie(title, timestamp)


def prompt_watched_movie():
    username = input("username: ")
    movie_id = input("Movie id: ")
    database.watch_movie(username, movie_id)


def print_movie_list(movies):
    print(f"{'id':{5}}{'Release Date':<{20}}{'Title'}")
    for _id, title, release_date in movies:
        rel_date = datetime.datetime.fromtimestamp(release_date)
        parsed_date = rel_date.strftime("%d-%b-%Y")
        print(f"{_id:<{5}}{parsed_date:{20}}{title}")
    print("")


def show_movies_list(header, movies):
    print(f"-- Showing {header} movies --")
    print_movie_list(movies)


def show_watched_list(username, movies):
    print(f"-- {username}'s watched movies --")
    if movies:
        # print_movie_list(movies)
        for movie in movies:
            print(movie)


menu = """
1) Add new movie
2) View upcoming movies
3) View all movies
4) Watch a movie
5) See watched list
6) Create a new user

x) Exit

=> """


while (user_input := input(menu)) != "x":
    if user_input == "1":
        prompt_add_movie()

    elif user_input == "2":
        movies = database.get_movies(True)
        show_movies_list("upcoming", movies)

    elif user_input == "3":
        movies = database.get_movies()
        show_movies_list("ALL", movies)

    elif user_input == "4":
        prompt_watched_movie()

    elif user_input == "5":
        username = input("username: ")
        movies = database.get_watched_movies(username)
        show_watched_list(username, movies)

    elif user_input == "6":
        prompt_add_user()

    else:
        print("Invaid input. Please try again.")
