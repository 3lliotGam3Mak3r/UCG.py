# ask for name
name = str(input("What is your Name?: "))
# ask for age
age = int(input("What is your Age?: "))
# ask favorite hobby
hobby = str(
    input(
        "What is your favorite Hobby?(eg. playing outside, hanging out with friends, etc.): "
    )
)


# define function
def make_Profile(a, e, i):

    print(" ")

    # display info
    print(f"\nHi! My name is {a}!")

    print(f"I am {e} years old.")

    print(f"I love {i}\n")


make_Profile(name, age, hobby)
