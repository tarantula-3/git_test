import json

def get_number(filename):
    number = int(input("What's your favorite number? "))
    f_obj = open(filename, "w")
    json.dump(number, f_obj)
    f_obj.close()

def show_number(filename):
    f_obj = open(filename)
    number = json.load(f_obj)
    print(f"I know your favorite number! It's {number}")
    f_obj.close()

try:
    filename = "fav_num.json"
    f_obj = open(filename)
except FileNotFoundError:
    get_number(filename)
else:
    show_number(filename)
