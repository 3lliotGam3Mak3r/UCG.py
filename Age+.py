#asking for user input variables
Age = int(input("What is your age?: "))
Height = float(input("\nWhat is your height?(In inches): "))

def ageheight():
    print(f"\nAge: {Age}, Height: {Height} in\n")
#evaluates input to determine if the user is eligible for rides
if Age < 5:
    ageheight()
    print("You Are Too Young For Rides.")
elif Age >= 5 and Height < 36:
    ageheight()
    print("You Can Only Ride Kiddie Rides")
elif Age >= 10 and Height >= 48:
    ageheight()
    print(" Can Ride ALL Attractions, Roller Coasters Included") 
else:
    ageheight()
    print("Can Ride MOST Attractions, CANNOT Ride Roller Coasters")
