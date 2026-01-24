s = input("Enter a string: ")

def is_palindrome(string):
    x = ""
    for char in string:
        if char.isalnum():
            x += char.lower()
    return x == x[::-1]

if is_palindrome(s):
    print(f'"{s}" is a palindrome.')
else:
    print(f'"{s}" is not a palindrome.')