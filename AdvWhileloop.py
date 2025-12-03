# This set includes 4 assignments, increasing in difficulty:
# 1️⃣ Basic Level
# 2️⃣ Intermediate Level
# 3️⃣ Advanced Level
# 4️⃣ Expert Level

# Rules:
# - You must use WHILE LOOPS for iteration.
# - Do NOT use for loops unless explicitly stated.
# - Add input validation or error handling where appropriate.


# =========================================================
# 1️⃣ BASIC LEVEL
# ---------------------------------------------------------
# TODO: Write a function `count_to_n` that:
# - Takes an integer n
# - Prints numbers from 1 to n using a while loop
# Example: count_to_n(5) → prints 1 2 3 4 5

def count_to_n(n):
    num = 0
    while n > num:
        num += 1
        print(num)
count_to_n(5)

# =========================================================
# 2️⃣ INTERMEDIATE LEVEL
# ---------------------------------------------------------
# TODO: Write a function `sum_until_zero` that:
# - Continuously asks the user for integers
# - Adds them to a total
# - Stops when the user enters 0
# - Returns the total sum
# Example (input): 4, 5, -3, 0 → returns 6

def sum_until_zero():
    numbers = int(input("Please input a number:"))
    totality = 0
    while numbers != 0:
        totality += numbers
        numbers = int(input("Please input a number:"))
    else:
        print(totality)
sum_until_zero()


# =========================================================
# 3️⃣ ADVANCED LEVEL
# ---------------------------------------------------------
# TODO: Write a function `reverse_string` that:
# - Takes a string
# - Uses a while loop to reverse it manually
# - Returns the reversed string
# Example: reverse_string("Python") → "nohtyP"

def reverse_string(text):
    txtlen = len.text
    while txtlen > 0:
        i = txtlen
        i2 = txtlen - 1
        
        



# =========================================================
# 4️⃣ EXPERT LEVEL
# ---------------------------------------------------------
# TODO: Write a function `guess_the_number` that:
# - Randomly selects a number between 1 and 50
# - Repeatedly asks the user to guess until correct
# - Tells the user if the guess is too high or too low
# - Prints number of attempts when correct
# Example:
# Computer selects 17
# User guesses 10 → "Too low"
# User guesses 20 → "Too high"
# User guesses 17 → "Correct! You guessed in 3 tries!"

import random

def guess_the_number():
    pass


# =========================================================
# ✅ TEST AREA (uncomment for local testing)
# ---------------------------------------------------------
# count_to_n(5)
# print(sum_until_zero())   # Interactive
# print(reverse_string("Python"))
# guess_the_number()        # Interactive
