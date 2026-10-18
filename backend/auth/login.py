import json as js

def login():

    username = input("Enter your username: ")
    password = input("Enter your password: ")

    with open("data/users.json", "r") as file:
     data = js.load(file)

    for user in data["users"]:
     if user["username"] == username and user["password"] == password:
      return username