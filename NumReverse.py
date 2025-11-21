print("Welcome to the number reverser!")
#Asks user for a Number that the code will reverse
number = str(input("Please input a number: "))

#Makes a variable to store the reversed number
numrev = ""

#finds the digit of the number and counts backwards
i = len(number) - 1

#starts a while loop to calculate the reversed number
while i >= 0:

    #stores the reversed number
    numrev = numrev + number[i]
    #counts a digit backward to prevent an infinite loop
    i-=1

#prints the result
print(f"The number reversed is {numrev}")

