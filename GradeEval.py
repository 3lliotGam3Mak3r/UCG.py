#Program Description: This program eavlutes student grade

#Getting the grade from the user

test_score = float(input("Enter your test score 0-100: "))

#If and else if statements to assign grade to user depending on score
#and printing letter grade correctly.

if test_score >= 90:
    print("Your grade is an A ")
elif test_score >= 80:
    print("Your grade is a B")
elif test_score >= 70:
    print("Your grade is a C")
elif test_score >= 60:
    print("Your grade is a D")
else:
    print("Your grade is an F")