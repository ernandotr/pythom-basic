def gcd(a, b):
    """Calculate the Greatest Common Divisor (GCD) of two integers a and b."""
    while b:
        a, b = b, a % b
    return abs(a)

# Example usage
if __name__ == "__main__":
    num1 = 48
    num2 = 18
    print(f"The GCD of {num1} and {num2} is {gcd(num1, num2)}") # Output: The GCD of 48 and 18 is 6
    num1 = 56
    num2 = 98    
    print(f"The GCD of {num1} and {num2} is {gcd(num1, num2)}") # Output: The GCD of 56 and 98 is 14