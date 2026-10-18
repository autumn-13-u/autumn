from backend import lobby
import os
import json as js
username = None
def autumn(username):#it defines a function that only works after the user is logged in
    print(f"Welcome, {username}!")
username = username
def remember(username):
 memory = input("What should I remember? ")
 file_path = os.path.join("data", "databases", username + ".json")
 with open(file_path, "r") as file:

  data = js.load(file)#converts .json to python file
  data["memories"].append(memory)#add the new python data

#write the changed data back to the .json file
  with open(file_path, "w") as file:
    js.dump(data, file, indent=4)



if __name__ == "__main__":
 lobby.lobby()



