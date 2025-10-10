# Challenge: Implement error handling to ensure that the user enters a non-negative number for the time duration.

#=======================================================

#Input: Prompt the user to enter a time duration in hours.

try:
    hours = float(input("Please enter the time duration in hours: "))

    if hours<0:
        print("Error: The time duration must be a positive number.")

    # Process: Convert the time duration to minutes and seconds.
    else:
        minutes = int(hours*60)
        seconds = round((hours*60-minutes)*60)

        # Output: Display the converted time duration in minutes and seconds.
        print(f"{hours} hours = {minutes} minutes and {seconds} seconds")

except ValueError:
    print("Error: Please enter numeric values only.")


