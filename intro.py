#makes the variables
var1 = False

name = "Elliot"

age = "16 1/2"

hobby = "playing video games"

food = "pizza"

#makes a variable to stop my while loop
stopper = int(0)

#Creates a function to make a line
def line():
    print("-" * 20)

line


#prints information about me
print("Hello my name is Elliot\n")

print("I am 16 1/2 years old\n")

print("My favorite hobby is playing video games\n")

print("I like to eat pizza!\n")

input = str(input(f"your name is {name}, you are {age} years old, your hobby is {hobby}, and your favorite food is {food}, Correct?"))

#malkes my first if statement
if input == "no" or input == "No":
    var1 = False
    print("Then why did you type it out in the code? \n-_-")
elif input == "yes" or input == "Yes":
    var1 = True
    print("Thought so, Thanks!")
else:
    print("What?")

#prints the same message over for 20 times
while var1 == True and stopper <= 20:
    print("\nThanks 𓁹 ‿𓁹")
    stopper = (stopper + 1)

line