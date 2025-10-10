

#Input: Prompt the user to enter the principal amount, interest rate (in percentage), and the time period (in years).
principle = float(input("Enter the principle amount: "))
rate = float(input("Enter the interest rate (in %): "))
time = float(input("Enter the time period (in years): "))

#Processing: Calculate the simple interest using the formula: Simple Interest = (Principal * Rate * Time) / 100.

simple_interest = (principle * rate * time) / 100

#Output: Display the calculated simple interest.

print("The calculated simple interest is: ", simple_interest)
