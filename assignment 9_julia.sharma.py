#Challenge: Ensure that the user enters only a single character and handle cases where the input is not a letter.

#=====================================================


#Output: Display whether the entered character is a vowel or a consonant.
...

# Input: Ask the user to etter a letter
char_input = input("Please enter a single character: ")

#I need to check if the input is exactly one character and is a letter
if len(char_input)==1 and char_input.isalpha():
    #convert the character the user entered into a lowercase
    char = char_input.lower()

    #check if the input is a vowel or a consonant
    if char in "aeiou":
       print("The character is a vowel.")
    else:
        print("The character is a consonant.")

else:
    if len(char_input) != 1:
        print("Error. Please enter only one character.")
    else:
        print("Error: The input is not a letter.")