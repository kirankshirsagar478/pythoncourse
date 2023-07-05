def is_palindrome(s):
    # Remove any spaces and convert the string to lowercase
    s = s.replace(" ", "").lower()
    
    # Compare the string with its reversed version
    return s == s[::-1]

# Example usage
string = "Madam Arora teaches malayalam"
if is_palindrome(string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
