#Challenge: Use a loop structure to compare characters from both ends of the string to determine whether it is a palindrome.

#===================================
#Description: Write a program that prompts the user to enter a string and then checks whether it is a palindrome. A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward.

#Prompt user to enter a string
print()
print("Welcome to the Palindrome Tester!")
print()
print("Please enter a string: ")
user_input = input()

#make lowercase and remove spaces and punctuation
cleaned = "".join(ch.lower() for ch in user_input if ch.isalnum())

#Check to see if input is a palindrome
i,j = 0, len(cleaned)-1 #two pointers

is_palindrome = True #assumes string is palindrome
#Loop to compare characters from each end
while i<j:
    if cleaned[i] != cleaned[j]: #mismatch found
        is_palindrome = False
        break
    i += 1
    j-= 1

if is_palindrome:
    print("Yes, it's a palindrome!")
else:
    print("No, it is not a palindrome.")