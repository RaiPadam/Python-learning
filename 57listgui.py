def add_two_numbers():
    try:
        number1 = int(input("Enter first number: "))
        number2 = int(input("Enter second number: "))
        total = number1 + number2
        print(f"Total is {total}")
    except ValueError:
        print("Please enter valid integers.")

add_two_numbers()