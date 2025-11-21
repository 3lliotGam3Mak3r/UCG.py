def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mult(a, b):
    return a * b
def div(a, b):
    return a / b
def modulus(a, b):
    return a % b
def expo(a, b):
    return a ** b
    

n1=float(input("Enter the first number: "))
         
n2=float(input("Enter the second number: "))

print(f"The numbers {n1} & {n2} added is {add(n1,n2)}")
print(f"The numbers {n1} & {n2} subtracted is {sub(n1,n2)}")
print(f"The numbers {n1} & {n2} multiplied is {mult(n1,n2)}")
print(f"The numbers {n1} & {n2} divided is {div(n1,n2)}")
print(f"The numbers {n1} & {n2} in modulus is {modulus(n1,n2)}")
print(f"The numbers {n1} & {n2} exponentiation is {expo(n1,n2)}")