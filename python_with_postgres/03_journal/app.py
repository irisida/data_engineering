from db import create_tables, add_entry, get_entries

menu = """Please select one of the following options:

1) Add New Entry for today.
2) View Entries
3) Exit
=>  """


def prompt_new_entry():
    content = input("Subject studied today: ")
    entry_date = input("Date: ")
    add_entry(content, entry_date)


def view_entries(entries):
    for entry in entries:
        print(f"{entry[1]:<{12}}{entry[0]}")


# initialise the database
create_tables()

while (user_input := input(menu)) != "3":
    if user_input == "1":
        prompt_new_entry()

    elif user_input == "2":
        view_entries(get_entries())
    else:
        print("Invalid option. Please try again")
