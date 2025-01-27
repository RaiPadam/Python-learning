# Function to calculate the sum of three numbers
def sum_of_three_numbers(num1, num2, num3):
    total = num1 + num2 + num3
    # Print the total
    print(f"The total sum is: {total}")
    return total

# Input numbers
number1 = 5
number2 = 10
number3 = 15

# Call the function and store the result
result = sum_of_three_numbers(number1, number2, number3)

# Print the returned value (optional, since it's already printed inside the function)
print(f"Returned total: {result}")