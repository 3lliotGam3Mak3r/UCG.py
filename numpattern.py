#This program asks the user for a number
# and then repeats the number as many times as the number input
#Example: 
#user input = 3, 
#1
#22
#333

#Gets the users number
n = int(input("Please input a number: "))

#variable to help repeating
i = 1

#while loop to start the pattern
while i <= n:
    #prints the number "number" times
    print(str(i) * i)

    #prevents infinite loop and helps with the repetition
    i += 1