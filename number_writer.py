import json
from random import randint

number = [randint(0, 20) for x in range(10)]

file_name = "number.json"
f_obj = open(file_name, "w")
json.dump(number, f_obj)
