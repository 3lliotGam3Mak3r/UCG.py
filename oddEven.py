
print("Welcome to ODD or EVEN! \nThe Program that checks if the number is ODD or EVEN")
print("-" * 30)


number = int(input("Please input a number: "))

def oddEven(a):
    if a % 2 == 0:
        print(f"{a} is an EVEN NUMBER!")

    else:
        print(f"{a} is an ODD NUMBER!")

oddEven(number)