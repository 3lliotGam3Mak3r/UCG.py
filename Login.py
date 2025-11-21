password = "qwerty"
attempt = ""
tries = 0

while attempt != password and tries < 3:
    attempt = input("Please input your password: ")
    tries += 1

    if attempt != password:
        print("Wrong. Try again.")
        
if attempt == password:
    print("Welcome User!")
else:
    print("Youve run out of tries. \nplease try again later.")
