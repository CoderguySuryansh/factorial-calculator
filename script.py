def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Get input from the user
number = int(input("Enter a number to calculate its factorial: "))

# Calculate the factorial
result = factorial(number)

# Display the result
print(f"The factorial of {number} is {result}")
