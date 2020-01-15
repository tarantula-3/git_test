import json

file_name = "number.json"
f_obj = open(file_name, "r")
numbers = json.load(f_obj)

print(numbers)
