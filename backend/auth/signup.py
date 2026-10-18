import json as js
import os
def signup():

 if not os.path.exists("data/databases"):#checks if the path exists
  os.mkdir("data/databases")#creates the folder if it does not exist


 username = input("Create a username: ")#creates a user
 password = input("Create a password: ")#creates a password

 file_path = os.path.join("data", "databases", username + ".json")#figures out where the file should be
 with open(file_path, "w") as file:#opens the users .json file
    js.dump({"memories": []}, file, indent=4)#writes {"memories": []} in the .json file
    
 with open("data/users.json", "r") as file :
  data = js.load(file)


  #assigns the users credentials to a variable
  data["users"].append({
     "username": username,
     "password": password
 })

 with open("data/users.json", "w") as file: #writes data in the users.json file
  js.dump(data, file, indent=4)
  print("Account creation sucessful 😊")