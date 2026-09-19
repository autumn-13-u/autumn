import json as js
def login():#put this code into a function to be able to use return

 username = input("Enter your username: ")
 password = input("Enter your password: ")

 with open("data/users.json", "r") as file:#reads the json file
  data = js.load(file)#loads json data

 for user in data["users"]:#checks every user for the matching password and user
  if user["username"] == username and user["password"] == password:#checks if the password and user are correct
   return username #sends a signal
username = login()#catches the signal and saves it
import main
print("IMPORTED:", main)
print("PATH:", main.__file__)

main.lobby(username)
import os
file_path = os.path.join("data", "databases", username + ".json")

with open(file_path, "r") as file:  # opens the logged-in user's database and reads it
 data = js.load(file)# loads the database into Python

