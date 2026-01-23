s = input("Enter a string: ")

def is_palindrome(string):
    cleaned_string = ''.join(char.lower() for char in string if char.isalnum())
    return cleaned_string == cleaned_string[::-1]
if is_palindrome(s):
    print(f'"{s}" is a palindrome.')
else:
    print(f'"{s}" is not a palindrome.')