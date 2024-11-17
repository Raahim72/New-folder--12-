def check_natural_number(num):
    if isinstance(num, int) and num > 0:
        return True
    else:
        return False

# Input from user
number = input("Enter a number: ")

# Try to convert the input to an integer
try:
    number = int(number)
    if check_natural_number(number):
        print(f"{number} is a natural number.")
    else:
        print(f"{number} is not a natural number.")
except ValueError:
    print("Please enter a valid integer.")
