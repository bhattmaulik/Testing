# Function to find whether a number is even or odd
def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
    # Test the function with some examples
print(check_even_odd(4))  # Output: Even
print(check_even_odd(7))  # Output: Odd