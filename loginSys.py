import json

def initUsers() -> dict:
    with open("data.json", "r") as file: 
        data = json.load(file)

    return data

def addUser(users:dict): 
    username = input("\n Username: ")
    password = input(" Password: ")
    
    while True: 
        if username not in users: 
            users[username] = {
                "password": password, 
                "items": []
            }

            with open("data.json", "w", encoding="utf-8") as file: 
                json.dump(users, file, indent=4)

            print("\nUser added")
            break
        
        else: 
            print("\nUser already exists. Please try again.")

def login(users):
    while True:
        username = input("\n Username: ")
        password = input(" Password: ")

        if username in users and users[username]["password"] == password:
            print(f"\nWelcome {username}")
            return {"username": username, "data": users[username]}
        
        else:
            print("\nInvalid username or password\n")
            
            while True:
                print(" r) Try again")
                print(" q) Quit\n")

                option = input("Option: ")

                if option == "r":
                    break # "break" will exit the inner loop and return to the outer
                elif option == "q":
                    return None # "break" will not exit the function entirely
                else:
                    print("\nInvalid option. Please try again.")

def userSession(user):
    username = user["username"]
    data = user["data"]

    listItems(data["items"])

    while True:
        print("Select an action\n")
        print(" a) Add item")
        print(" l) List items")
        print(" q) Log out\n")

        option = input("Option: ")

        if option == "a":
            addItem(user)

        elif option == "l":
            listItems(data["items"])

        elif option == "q":
            print(f"\nLogging out {username}\n")
            break

        else:
            print("\nInvalid option. Please try again.\n")

def listItems(items):
    print("\nThese are your items:")

    for i, item in enumerate(items, 1):
        print(f"{i}) {item}")

    print("")

# add data to json file
def addItem(user):
    username = user["username"]
    data = user["data"]
    new_item = input("\nAdd item: ")
    data["items"].append(new_item)

    with open("data.json", "r+") as file:
        users = json.load(file)
        users[username]["items"] = data["items"]
        file.seek(0)
        json.dump(users, file, indent=4)
        file.truncate()
    
    listItems(data["items"])

def main():
    users = initUsers()
    print("Welcome to Lagra (TM)\n")

    while True:
        print(" l) Log in")
        print(" r) Register")
        print(" q) Quit\n")

        option = input("Option: ")

        if option == "l":
            if user := login(users):
                userSession(user)

        elif option == "r": 
            addUser(users)       

        elif option == "q":
            break
        
        else:
            print(option)
            print("\nInvalid option. Please try again.\n")

main()