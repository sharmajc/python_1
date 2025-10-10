#Challenge: Implement error handling to ensure that the user enters a positive integer for the age.

#==================================
#Input: Prompt the user to enter their age.
#Processing: Classify the age into different categories:
#Under 18: Minor
#18-65: Adult
#Above 65: Senior citizen
#Output: Display the category based on the entered age.
...
#ask the user to enter their age
age_input = input("Please enter your age: ")

# check if the input is a number and is not empty response/string
if age_input.isdigit():
    age = int(age_input)

    #make sure that the age is positive
    if age>0:
        #classify the age below
        if age <18:
            print("Minor")
        elif 18<= age <= 65:
            print("Adult")
        else: #if they'are above 65
            print("Senior Citizen")
    else:
        print("Error: Age must be a positive number.")
else:
    print("Error: Invalid input. Please enter a positive number.")