def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Input from the user
num = int(input("Enter a number: "))

# Check if the input is non-negative
if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    result = factorial(num)
    print(f"The factorial of {num} is {result}")
