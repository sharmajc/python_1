#Challenge: Handle cases where the user enters non-numeric input for the year and provide appropriate error messages.

#===============================================

#Input: Prompt the user to enter a year.
try:
    year = int(input("Please enter the year: "))
    #Processing: Determine whether the entered year is a leap year or not. A leap year is divisible by 4 but not by 100 unless it is also divisible by 400.
    if (year % 4 == 0 and year % 100 !=0) or (year % 400 ==0):
    #Output: Display whether the entered year is a leap year or not.
        print("Leap year.")
    else:
        print("Not a leap year.")
except ValueError:
    print("Error: Please enter a numeric value only.")