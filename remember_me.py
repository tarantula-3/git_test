import json

def get_stored_username():
    """Get stored username if available"""
    filename = "username.json"
    try:
        f_obj = open(filename)
        username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    username = input("What's your name? ")
    filename = "username.json"
    f_obj = open(filename, "w")
    json.dump(username, f_obj)
    print(f"We'll remember you when you com back {username}!")

def verify_user(username):
    print(f"Is your name {username}?")
    user = input("> ")
    if user.lower() == "yes":
        print(f"Welcome back, {username}!")
    else:
        get_new_username()

def greet_user():
    username = get_stored_username()

    if username:
        verify_user(username)
    else:
        get_new_username()


greet_user()
