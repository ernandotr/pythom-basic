def lcm(a, b):
    """Calculate the Least Common Multiple (LCM) of two integers a and b."""
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x

    return abs(a * b) // gcd(a, b) if a and b else 0

# Example usage
if __name__ == "__main__":
    num1 = 12
    num2 = 15
    print(f"The LCM of {num1} and {num2} is {lcm(num1, num2)}") # Output: The LCM of 12 and 15 is 60
    num1 = 12
    num2 = 4    
    print(f"The LCM of {num1} and {num2} is {lcm(num1, num2)}") # Output: The LCM of 12 and 4 is 12