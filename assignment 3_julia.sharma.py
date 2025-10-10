#Challenge: Provide feedback to the user based on their BMI category (e.g., underweight, normal weight, overweight, obese).

#Input: Prompt the user to enter their weight in kilograms and height in meters.
weight_input = input("Enter your weight in kilograms: ")
height_input = input ("Enter your height in meters: ")

# Convert the values to numbers/float
weight = float(weight_input)
height = float(height_input)

#Processing: Calculate the BMI using the formula: BMI = Weight / (Height^2).
bmi = weight / (height **2)

#Output: Display the calculated BMI.
print("your BMI is: ", bmi)

if bmi <18.5:
    print("You are underweight.")
elif bmi <=24.9:
    print("You are normal weight.")
elif bmi <=29.9:
    print("You are overweight.")
elif bmi <=34.9:
    print("You are Class I Obese.")
elif bmi <=39.9:
    print("You are Class II Obese.")
elif bmi >=40:
    print("You are Class III obese.")
