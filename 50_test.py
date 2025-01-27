def square_even_numbers(numbers):
    """
    # Takes a list of numbers and returns a new list containing
    the squares of all even numbers from the original list.
    """
    # Use a list comprehension to find squares of even numbers
    return [num ** 2 for num in numbers if num % 2 == 0]

# Example usage
original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squared_evens = square_even_numbers(original_list)
print("Original list:", original_list)
print("Squared even numbers:", squared_evens)