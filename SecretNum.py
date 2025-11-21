SecrNum = 7
print("You have three tries!")
usrGuess = int(input("Guess a number between 1 & 10: "))
tries = 3

while usrGuess != SecrNum:
    if usrGuess > SecrNum:
        print("Too high!")
        tries -= 1
    elif usrGuess < SecrNum:
        print("Too low!")
        tries -= 1
    if tries == 0:
        print("Out of tries, sorry!")
        print(f"Number was: {SecrNum}")
        break    
    usrGuess = int(input("Guess a number between 1 & 10: "))
    

else:
    print(f"Correct! the number was {SecrNum}")

