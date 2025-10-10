#Challenge: Implement error handling to ensure that the user enters valid marks (between 0 and 100) for each subject.

#=================================================
#Input: Ask the user to enter their marks for three subjects.
#Processing: Calculate the average of the marks. Determine the grade based on the average:
#90 and above: A
#80-89: B
#70-79: C
#60-69: D
#Below 60: F
#Output: Display the calculated grade.

try:
    # Prompt user to enter their grades for three subjects
    subj_1 = float(input("Please enter your marks for subject 1: "))
    if not (0 <= subj_1 <= 100):
        print("Error: Marks must be between 0 and 100.")
        exit()

    subj_2 = float(input("Please enter your marks for subject 2: "))
    if not (0 <= subj_2 <= 100):
        print("Error: Marks must be between 0 and 100.")
        exit()

    subj_3 = float(input("Please enter your marks for subject 3: "))
    if not (0 <= subj_3 <= 100):
        print("Error: Marks must be between 0 and 100.")
        exit()

    # Calculate the average of the marks.
    average = (subj_1+subj_2+subj_3)/3

    # Determine the grade
    if average >= 90:
        grade ="A"
    elif average >= 80:
        grade = "B"
    elif average >=70:
        grade = "C"
    elif average >=60:
        grade = "D"
    else:
        grade = "F"

    #Output
    print(f"Your average is: {average:.2f}")
    print(f"Your grade is: {grade}")

except ValueError:
    print("Error: Please enter numeric values only.")