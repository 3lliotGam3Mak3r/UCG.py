#This program gets a number from the user, squares it, and then prints the squared number

#This gets the number from the user
num = float(input("Please enter a number: "))

#Defines a function with the parameter of the number the user input
def square(num):

    #Squares number when function is called
    sqnum = num * num

    #Prints Squared number when function is called
    print(sqnum)

#Calls function
square(num)