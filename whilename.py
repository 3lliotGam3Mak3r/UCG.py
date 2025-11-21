import time
#gets the users name
name = input("Please enter your Name: ")

#starts the while loop, detecting when the name variable is empty
while name == "" or not name.isalpha(): 
    time.sleep(1)  
    print("Access Denied")
    time.sleep(.5)
    print("Be sure there are no number characters in your name")
    print("Be sure to fill out a valid response")
    time.sleep(.5)
    name = input("Please enter your Name: ")

else:
    print(f"Welcome {name}")
