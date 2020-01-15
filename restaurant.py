class Restaurant():
    def __init__(self):
        self.restaurant_name = input("Restaurant name: ")
        self.cuisine_type = input("Cuisine type: ")
        self.number_served = 0

    def describe_restaurant(self):
        print(f"The restaurant name: {self.restaurant_name}")
        print(f"Its cuisine type is {self.cuisine_type}")

    def open_restaurant(self, is_open):
        if is_open:
            print("The restaurant is now open.")
        else:
            print("The restaurant is not available at the moment.")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, number):
        self.number_served += number
        print(f"Customers served in one day of business:\
 {self.number_served}")


class IceCreamStand(Restaurant):
    def __init__(self):
        super().__init__()
        self.flavors = [
            "vanilla",
            "chocolate",
            "coconut",
            "banana",]

    def show_flavors(self):
        print("Flavors available:")
        for flavor in self.flavors:
            print(f"- {flavor}")


test = Restaurant()
test.describe_restaurant()

print(f"Customers served: {test.number_served}")

test.number_served = 10
test.open_restaurant(True)
print(f"Customers served: {test.number_served}")

test.set_number_served(int(input("> ")))
print(f"Customers served: {test.number_served}")
test.increment_number_served(int(input("> ")))

test = IceCreamStand()
test.show_flavors()
