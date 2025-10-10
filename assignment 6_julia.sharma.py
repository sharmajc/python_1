#Input: Ask the user to enter an amount in one currency (e.g., USD).
try:
    usd = float(input("Please enter the amount in USDs: "))

    #Processing: Convert the amount to another currency (e.g., EUR) using a fixed exchange rate.
    if usd <0:
        print("Error: please enter a positive number.")

    else:
        npr = (usd * 140.26)

        # Output: Display the converted amount in the target currency.

        print(f"{usd} USD = {npr} Nepalese Rupees")

except ValueError:
    print("Error: Please enter a numeric value only.")