#Advanced Python Assignment: Mastering For Loops
#------------------------------------------------
#Complete each TODO using for loops only.
#You may use range(), enumerate(), zip(), or list comprehensions where appropriate.

#Focus on:
#- Iteration over sequences
#- Nested loops
#- Conditional logic inside loops
#- Loop control (break, continue)
#- List / dict comprehensions

#Each task includes a description and example.

# 1️⃣ BASIC ITERATION
# TODO: Write a function `count_vowels` that:
# - Takes a string input
# - Counts and returns the number of vowels (a, e, i, o, u)
# Example: count_vowels("education") → 5

def count_vowels(text):
    vowel= "a","e","i","o","u"
    nums = 0
    for char in text:
        if char in vowel:
            nums += 1
            print(char)
    return nums
print(count_vowels("pizza"))

# 2️⃣ RANGE LOOP
# TODO: Write a function `squares_list` that:
# - Takes an integer n
# - Returns a list of the squares of numbers from 1 to n (inclusive)
# Example: squares_list(5) → [1, 4, 9, 16, 25]

def squares_list(endnum):
    sqlist = []
    number = 1
    while number <= endnum:
        sqnum = number * number
        sqlist += sqnum
        number += 1
    print(sqlist)        
squares_list(4)
squares_list(12)


# 3️⃣ LOOP WITH CONDITIONALS
# TODO: Write a function `filter_even_numbers` that:
# - Takes a list of integers
# - Returns a new list containing only the even numbers
# Example: filter_even_numbers([1, 2, 3, 4, 5, 6]) → [2, 4, 6]

def filter_even_numbers(numbers):
    pass


# 4️⃣ NESTED LOOPS
# TODO: Write a function `multiplication_table` that:
# - Takes an integer n
# - Returns a list of lists representing an n×n multiplication table
# Example: multiplication_table(3) → [[1,2,3],[2,4,6],[3,6,9]]

def multiplication_table(n):
    pass


# 5️⃣ ENUMERATE & LOOP CONTROL
# TODO: Write a function `find_first_negative` that:
# - Takes a list of integers
# - Returns a tuple (index, value) of the first negative number found
# - If no negative number exists, return None
# Example: find_first_negative([3, 4, -2, 7]) → (2, -2)

def find_first_negative(numbers):
    pass


# 6️⃣ ZIP & ITERATION
# TODO: Write a function `combine_lists` that:
# - Takes two lists of equal length
# - Returns a dictionary mapping elements from the first list to the second
# Example: combine_lists(["a", "b", "c"], [1, 2, 3]) → {"a": 1, "b": 2, "c": 3}

def combine_lists(keys, values):
    pass


# 7️⃣ LOOP + STRING PROCESSING
# TODO: Write a function `reverse_words` that:
# - Takes a sentence string
# - Returns a string where the order of words is reversed
# Example: reverse_words("Python is awesome") → "awesome is Python"

def reverse_words(sentence):
    pass


# 8️⃣ COMPREHENSION CHALLENGE
# TODO: Write a one-line list comprehension function `flatten_matrix` that:
# - Takes a 2D list (list of lists)
# - Returns a single flattened list
# Example: flatten_matrix([[1, 2], [3, 4], [5, 6]]) → [1, 2, 3, 4, 5, 6]

def flatten_matrix(matrix):
    pass


# 9️⃣ LOOP WITH AGGREGATION
# TODO: Write a function `word_frequency` that:
# - Takes a string sentence
# - Returns a dictionary where keys are words and values are counts
# - Ignore punctuation, treat words as lowercase
# Example: word_frequency("Python is fun and Python is powerful")
#          → {'python': 2, 'is': 2, 'fun': 1, 'and': 1, 'powerful': 1}

def word_frequency(sentence):
    pass


# 🔟 CHALLENGE TASK
# TODO: Write a function `matrix_diagonal_sum` that:
# - Takes a square matrix (list of lists)
# - Returns the sum of its main diagonal elements
# Example: matrix_diagonal_sum([[1,2,3],[4,5,6],[7,8,9]]) → 15

def matrix_diagonal_sum(matrix):
    pass


# ✅ TEST AREA (uncomment to test your functions)
# print(count_vowels("Education"))
# print(squares_list(6))
# print(filter_even_numbers([1,2,3,4,5,6]))
# print(multiplication_table(4))
# print(find_first_negative([5, 7, -3, 9]))
# print(combine_lists(["x","y","z"], [9,8,7]))
# print(reverse_words("Python makes learning fun"))
# print(flatten_matrix([[1,2],[3,4],[5,6]]))
# print(word_frequency("Python is fun and Python is fun"))
# print(matrix_diagonal_sum([[1,2,3],[4,5,6],[7,8,9]]))