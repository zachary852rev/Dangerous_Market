import logging
from Dangerous_Modules import purchase_menu, profile_menu, atm_menu, signup, login, logged_in, logged_in_success


def main():
    logging.basicConfig(filename="Dangerous_Log.log", level=logging.DEBUG, format='%(asctime)s :: %(message)s')
    logging.info("Program started successfully.")

    print("_"*100)
    print("""
                 _____ _  _ ___  __   _____ _____   __
                |_   _| || | __| \ \ / / __| _ \ \ / /
                  | | | __ | _|   \ V /| _||   /\ V / 
                  |_| |_||_|___|   \_/ |___|_|_\ |_|                                          
 ______   _______  __    _  _______  _______  ______    _______  __   __  _______ 
|      | |   _   ||  |  | ||       ||       ||    _ |  |       ||  | |  ||       |
|  _    ||  |_|  ||   |_| ||    ___||    ___||   | ||  |   _   ||  | |  ||  _____|
| | |   ||       ||       ||   | __ |   |___ |   |_||_ |  | |  ||  |_|  || |_____ 
| |_|   ||       ||  _    ||   ||  ||    ___||    __  ||  |_|  ||       ||_____  |
|       ||   _   || | |   ||   |_| ||   |___ |   |  | ||       ||       | _____| |
|______| |__| |__||_|  |__||_______||_______||___|  |_||_______||_______||_______|
           __   __  _______  ______    ___   _  _______  _______                  
          |  |_|  ||   _   ||    _ |  |   | | ||       ||       |                 
          |       ||  |_|  ||   | ||  |   |_| ||    ___||_     _|                 
          |       ||       ||   |_||_ |      _||   |___   |   |                   
          |       ||       ||    __  ||     |_ |    ___|  |   |                   
          | ||_|| ||   _   ||   |  | ||    _  ||   |___   |   |                   
          |_|   |_||__| |__||___|  |_||___| |_||_______|  |___|                                                                                                                              
    """)
    print("-"*100)
    logging.info("ASCII logo loaded successfully.")

    while True:
        print("Please type a command and hit 'Enter.'")
        print("\t1) SIGN UP")
        print("\t2) LOG IN")
        print("\t3) EXIT")
        ch = int(input(">>> "))
        if ch == 1:
            signup()
        elif ch == 2:
            login()
            if logged_in == True:
                logged_in_success()
            else:
                print("You are not logged in!")

        elif ch == 3:
            return None
        else:
            print("That's not an acceptable number. Try again, dingus.")
            logging.info("User tried to enter an unrecognized number or command.")

if __name__ == '__main__':
    main()