class User():
    def __init__(self):
        self.first_name = input("First name: ").strip()
        self.last_name = input("Last name: ").strip()
        self.full_name = f"{self.first_name.title()} {self.last_name.title()}"
        self.age = int(input("Age: "))
        self.login_attemp = 0

    def greet_user(self):
        print(f"Hello, {self.full_name}, who are {self.age} years old")
        print("Thank you for chosing us")

    def increment_login_attemp(self):
        self.login_attemp += 1

    def reset_login_attemp(self):
        self.login_attemp = 0


class Administrator(User):
    def __init__(self):
        super().__init__()
        self.privileges = Privileges()


class Privileges():
    def __init__(self):
        self.privileges = [
            "can add post",
            "can delete post",
            "can ban user",
        ]

    def show_privileges(self):
        print(f"Admin's privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")


test = User()
test.greet_user()

for x in range(5):
    test.increment_login_attemp()
print(test.login_attemp)

test.reset_login_attemp()
print(test.login_attemp)

test = Administrator()
test.privileges.show_privileges()
