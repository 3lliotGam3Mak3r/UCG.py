# define function
def wordconvert(n):

    # if n equals 1
    if n == 1:
        w = "one"

    # if n equals 2
    elif n == 2:
        w = "two"

    # and so on
    elif n == 3:
        w = "three"

    elif n == 4:
        w = "four"

    elif n == 5:
        w = "five"

    # if the user doesnt enter a number
    else:
        print("That isn't a number between 1 and 5.")
        return

    # tells the user what the number is in word form
    print(f"The number {n} is written as: {w}")


# start the main program
try:

    # ask the user for a number 1-5
    num = input("Enter a number between 1 and 5: ")

    # convert from a string to an integer
    num = int(num)

    # call the function with the parameter (num)
    wordconvert(num)

# if the user inputs a string or a float, gives user an error message
except ValueError:
    print("That is not a whole number! Please input a whole number.")
