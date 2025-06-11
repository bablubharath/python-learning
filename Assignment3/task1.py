
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Sample number
number = int(input('Enter a number: '))
output = factorial(number)
print(f"The factorial of {number} is {output}")
