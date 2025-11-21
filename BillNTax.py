#gets all of my variables
bill = float(input("Enter the bill amount: $"))
split = float(input("How many people are splitting the bill? "))
tax = 0.0825
tip = 0.15

#Calculates the equations for me
taxA = bill * tax
tipA = bill * tip
total = bill + taxA + tipA
per_person = total / split

#prints all of my results
print(f"Bill ${bill:.2f}\nTax ${tax:.2f}\nTip ${tip:.2f}\nTotal Bill ${total:.2f}\nShare per person ${per_person:.2f}\nHave a Nice Day!")