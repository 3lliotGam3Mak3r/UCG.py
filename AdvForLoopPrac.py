"""
Python For-Loop Assignments (Student Version)
--------------------------------------------
Complete each of the following assignments. Do NOT include solutions in this file.
Produce your own Python code beneath each prompt.
"""

# BEGINNER LEVEL
# 1. Print each number from 1 to 20 using a for loop.
# Write your code below:

i = 1
for i in range(1,21):
    print(i)
    i += 1

print("\n")



# INTERMEDIATE LEVEL
# 2. Given a list of fruits, use a for loop to print only the fruits that have more than 5 letters.
fruits = ["apple", "kiwi", "banana", "pear", "pineapple", "plum"]
# Write your code below:
for word in fruits:
    if len(word) > 4:
        print(f"{word}\n")

print("\n")

# ADVANCED LEVEL
# 3. Using a for loop, count how many even and odd numbers exist in the list below.
numbers = [12, 5, 8, 19, 44, 2, 7, 18, 33, 50]
# Your code should print:
# "Even: X"
# "Odd: Y"
# Write your code below:
Even = 0
Odd = 0
for number in numbers:
    if number % 2 == 0:
        Even += 1
    else:
        Odd += 1
print(f"Even:{Even}\nOdd:{Odd}")

print("\n")

# EXPERT LEVEL
# 4. Nested for-loop challenge:
# Write a program that prints a multiplication table (1 through 10) in a grid format.
# Example (first 3 rows shown):
# 1 2 3 4 5 6 7 8 9 10
# 2 4 6 8 10 12 14 16 18 20
# 3 6 9 12 15 18 21 24 27 30
# Write your code below:


for i in range(1,11):
    for a in range(1,11):
        print(i*a, end=" ")
    print()
