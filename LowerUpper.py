# Mini Python program demonstrating lower(), upper(), and replace()

# Original string
text = "Hello Class! Python is Fun."

# Convert the string to all lowercase
lower_text = text.lower()
print("Lowercase:", lower_text)

# Convert the string to all uppercase
upper_text = text.upper()
print("Uppercase:", upper_text)

# Replace a word in the string
replaced_text = text.replace("Fun", "Awesome")
print("Replaced Text:", replaced_text)

# Combining methods: make all lowercase and replace 'python' with 'Java'
combined_text = text.lower().replace("python", "java")
print("Combined Methods:", combined_text)