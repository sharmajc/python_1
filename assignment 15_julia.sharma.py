#Challenge: Write the function using recursion.
#===================================
#Description: Create a function named is_palindrome that takes a string as input and returns True if it is a palindrome, and False otherwise.
...


def is_palindrome(string):
    cleaned = "".join(ch.lower() for ch in string if ch.isalnum()) #makes lowercase and removes spaces and punctuations
    #base case
    if len(cleaned) <= 1:
        return True
    #check if cleaned strings first and last character match
    if cleaned [0] != cleaned[-1]:
        return False
    #recursion that keeps checking next characters
    return is_palindrome(cleaned[1:-1])

print(is_palindrome("Madam, I'm Adam"))
print(is_palindrome("a"))
print(is_palindrome("Cat in a hat"))
