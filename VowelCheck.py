#1. Create a function that will count vowels in a piece of text
def countVowels(a):

#2. Inside the function, create a list of characters that are considered vowels
    vowel = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    
#3. Make a counter that starts at 0
    counter = 0

#4. Loop through the text one character at a time
    for char in userWord:

#5. Check whether the current character is a vowel
        if char in vowel:

#6. If the character is a vowel, increase the counter
            counter += 1

#7. After the loop ends, return the final number of vowels counted
    return counter

#8. Ask the user to type in a word or sentence
userWord = input("Please Enter A Word: ")

#9. Print the result inside a clear sentence and call your function and pass the user’s text into it
print(f"There are {countVowels(userWord)} vowels in {userWord}")
