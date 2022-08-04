import mysql.connector
import MySQL_Config as c
import hashlib
import logging

user_funds = 1000
user_role = "User"
user_spent = 0
user_inventory = []
logged_in = False

# Sign-up function
def signup():
    username = input("Enter desired username: ")
    pwd = input("Enter desired password: ")
    conf_pwd = input("Confirm desired password: ")
    if conf_pwd == pwd:
        enc = conf_pwd.encode()
        hash1 = hashlib.md5(enc).hexdigest()
        with open("Stored_Info.txt", "w") as f:
            f.write(username + "\n")
            f.write(hash1)
        f.close()
        print("You have been successfully registered into the Dangerous Market!")
        print("Please try logging in with the info you just entered.")
        logging.info("New user successfully entered into database.")
        return username
    else:
        print("Desired password does not match! \n")
        logging.info("New user tried to enter password that didn't match.")


# Log-in function
def login():
    logged_in = False
    username = input("Enter username: ")
    pwd = input("Enter password: ")
    auth = pwd.encode()
    auth_hash = hashlib.md5(auth).hexdigest()

    with open("Stored_Info.txt", "r") as f:
        stored_user, stored_pwd = f.read().split("\n")
    f.close()

    if username == stored_user and auth_hash == stored_pwd:
        print("Logged in successfully!")
        logging.info("User logged in successfully.")
        logged_in = True
        logged_in_success()
        return username
    else:
        print("Login failed, ya chump! \n")
        logging.info("User failed to login.")
        logged_in == False

# Main purchase menu, needs to connect to MySQL
def purchase_menu():
    global user_funds, user_inventory, user_spent, user_role
    logging.info("Opened purchase menu successfully.")
    while True:
        print("_"*100)
        print("\t1) Purchase \n\t2) View Your Inventory \n\t3) Go Back")
        pur_choice = input(">>> ")
        if pur_choice == "1":
            print("You currently have " + str(user_funds) + " gold.")
            purchase_inventory()

        elif pur_choice == "2":
            print("You currently have " + str(user_funds) + " gold.")
            print(user_inventory)

        else:
            return None


# Profile menu where you can view user name and edit roles
def profile_menu():
    global user_funds, user_inventory, user_spent, user_role
    while True:
        print("_"*100)
        print("\t1) View Profile \n\t2) Edit Roles \n\t3) View Friendlist \n\t4) Go Back")
        pro_choice = input(">>> ")

        if pro_choice == "1":
            file = open('Stored_Info.txt')
            content = file.readlines()
            content = content[0:-2]
            print("Your current username is zach.")
            print("Your current role is " + str(user_role) + ".")
            print("You currently have " + str(user_funds) + " Gold.")

        elif pro_choice == "2":
            print("Your current role is " + user_role + ".")
            print("\nWould you like to change it? \n\t1) Yes \n\t2) No")
            role_change = input(">>> ")
            if role_change == "1":
                user_role = "Admin"
                print("Your role has been changed to 'Admin.'")
            else:
                user_role = "User"
                print("No changes have been made.")

        elif pro_choice == "3":
            # Pulls first five rows from MySql table Customers
            print("Your current friends: ")
            cnx = mysql.connector.connect(user="root", password="zp90", host="127.0.0.1", database="p1")
            cursor = cnx.cursor()
            cus01 = "SELECT * FROM Customers WHERE cusID = 1;"
            cus02 = "SELECT * FROM Customers WHERE cusID = 2;"
            cus03 = "SELECT * FROM Customers WHERE cusID = 3;"
            cursor.execute(cus01)
            fa = cursor.fetchone()
            print(fa)
            cursor.execute(cus02)
            fa = cursor.fetchone()
            print(fa)
            cursor.execute(cus03)
            fa = cursor.fetchone()
            print(fa)

        else:
            break


# ATM menu to view and add funds
def atm_menu():
    global user_funds, user_inventory, user_spent, user_role
    while True:
        print("_"*100)
        print("\t1) Add funds \n\t2) View Wallet \n\t3) Go Back")
        atm_choice = input(">>> ")

        if atm_choice == "1":
            print("You currently have " + str(user_funds) + " Gold.")
            print("How much would you like to add?")
            add_funds = input(">>> ")
            user_funds = user_funds + int(add_funds)
            print("You currently have " + str(user_funds) + " Gold.")
            
        elif atm_choice == "2":
            print("You currently have " + str(user_funds) + " Gold.")

        else:
            break

# Backup inventory system for when MySQL stops working 
def show_inventory():
    global user_funds, user_inventory, user_spent, user_role
    while True:
        cnx = mysql.connector.connect(user="root", password="zp90", host="127.0.0.1", database="p1")
        cursor = cnx.cursor()
        inv01 = "SELECT * FROM Inventory WHERE itemID = 1;"
        inv02 = "SELECT * FROM Inventory WHERE itemID = 2;"
        inv03 = "SELECT * FROM Inventory WHERE itemID = 3;"
        inv04 = "SELECT * FROM Inventory WHERE itemID = 4;"
        inv05 = "SELECT * FROM Inventory WHERE itemID = 5;"
        cursor.execute(inv01)
        fa = cursor.fetchone()
        print(fa)
        cursor.execute(inv02)
        fa = cursor.fetchone()
        print(fa)
        cursor.execute(inv03)
        fa = cursor.fetchone()
        print(fa)
        cursor.execute(inv04)
        fa = cursor.fetchone()
        print(fa)
        cursor.execute(inv05)
        fa = cursor.fetchone()
        print(fa)

def purchase_inventory():
    # Pulls all entries from MySQL table Inventory
    global user_funds, user_inventory, user_spent, user_role
    while True:
        cnx = mysql.connector.connect(user="root", password="zp90", host="127.0.0.1", database="p1")
        cursor = cnx.cursor()
        inv01 = "SELECT * FROM Inventory WHERE itemID = 2;"
        inv02 = "SELECT * FROM Inventory WHERE itemID = 4;"
        inv03 = "SELECT * FROM Inventory WHERE itemID = 8;"
        inv04 = "SELECT * FROM Inventory WHERE itemID = 9;"
        inv05 = "SELECT * FROM Inventory WHERE itemID = 12;"
        cursor.execute(inv01)
        fa = cursor.fetchone()
        print(fa)
        cursor.execute(inv02)
        fa = cursor.fetchone()
        print(fa)
        cursor.execute(inv03)
        fa = cursor.fetchone()
        print(fa)
        cursor.execute(inv04)
        fa = cursor.fetchone()
        print(fa)
        cursor.execute(inv05)
        fa = cursor.fetchone()
        print(fa)
        print("Please enter the ID number of the item you'd like to purchase.")
        purchase_choice = input(">>> ")
        if purchase_choice == "1":
            user_inventory.append("Questionable Cheese")
            user_funds = user_funds - 50
            user_spent = user_spent + 50
            return user_funds, user_inventory, user_spent
        elif purchase_choice == "2":
            user_inventory.append("Nail Bread")
            user_funds = user_funds - 100
            user_spent = user_spent + 100
            return user_funds, user_inventory, user_spent
        elif purchase_choice == "3":
            user_inventory.append("Cursed Amulet")
            user_funds = user_funds - 200
            user_spent = user_spent + 200
            return user_funds, user_inventory, user_spent
        elif purchase_choice == "4":
            user_inventory.append("Midas Glove")
            user_funds = user_funds - 225
            user_spent = user_spent + 225
            return user_funds, user_inventory, user_spent
        elif purchase_choice == "5":
            user_inventory.append("Supersonic Hypercube")
            user_funds = user_funds - 300
            user_spent = user_spent + 300
            return user_funds, user_inventory, user_spent
        else:
            print("That is not a valid number, you fool!")
            return None



# Main menu after you log in, points to other functions that are called
def logged_in_success():     
    while True:
        print("\nWhat nefarious activities would you like to partake in today?")
        print("\n\t1) Buy Dangerous Items \n\t2) View/Edit Profile \n\t3) Add Funds \n\t4) Go Back")
        main_menu = input(">>> ")

        if main_menu == "1":
            purchase_menu()
        elif main_menu == "2":
            profile_menu()
        elif main_menu == "3":
            atm_menu()
        else:
            return None
    