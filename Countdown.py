import time

number = int(input("Enter a number to start the countdown!"))

while number > 0:
    print(number)
    time.sleep(0.5)
    number -= 1

print("TIME'S UP!")
