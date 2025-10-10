# Challenge: Implement error handling to ensure that the length and width entered by the user are positive numbers.

# =================================
#Input: Ask the user to enter the length and width of a rectangle.
#Processing: Calculate the area of the rectangle using the formula: .
#Output: Display the calculated area of the rectangle.
...

#Input
length = float(input("Enter length of the rectangle: "))
width = float(input("Enter width of the rectangle: "))

#Processing (with challenge)

area = length * width

#Output
if length >0 and width >0:
    print("The area of the rectangle is: ", area)
else:
    print("Error: Length and Width must be positive numbers.")
