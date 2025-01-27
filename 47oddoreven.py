def odd_even(num):
    if num % 2 == 0:
        print("Number is Even")
    else:
        print("Number is Odd")

try:
    num = int(input("Enter a number: "))
    odd_even(num)
except ValueError:
    print("Invalid input! Please enter a valid integer.")