print("Welcome to the Word reverser!")
print("We Don't Accept Palindromes")
#Asks user for a Number that the code will reverse
number = str(input("Please input a Word: "))

#Makes a variable to store the reversed number
wrdrev = ""

#Finds the finds the last character in the string
i = len(number) - 1

#Starts the while loop that will reverse the word
while i >= 0:

    #Starts typing the word in reverse
    wrdrev = wrdrev + number[i]
    #reduces the i variable so loop isnt infinite
    i-=1

#Prints the reversed word
print(f"The number reversed is {wrdrev}")

