#Challenge: Use nested loop structures to print the pattern efficiently and neatly. Allow the user to specify the character used for the pattern.

#=========================================
#Description: Develop a program that prompts the user to enter the number of rows for a pattern and then prints a pattern of asterisks (*) in the form of a right triangle
...

#prompt user to enter the number of rows
rows = int(input("Enter the number of rows for the triangle: "))
#Prompt user to enter the character
character = input("Enter the character to use in triangle: ")

#Count-Controlled Nested Loops
#Outer Loop for how many rows to print.
for i in range(1, rows+1):
    #Inner Loop for how many characters to put in each row.
    for j in range(i):
        print(character, end="") # Keeps characters on the same line
    print() #Moves to the next line after each row
