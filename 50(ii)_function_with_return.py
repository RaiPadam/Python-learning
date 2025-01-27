def total(n1,n2,n3):
    result = n1 + n2 + n3
    return result

n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
n3 = int(input("Enter the third number: "))

total_result = total(n1,n2,n3)
print(f"The total of{n1},{n2},{n3} is {total_result}")