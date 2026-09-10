# AI Generated Code: Tip & Split Calculator

# Function to calculate tip, total bill, and amount each person needs to pay
def calculate_bill(bill, tip_percentage, people):
    
    # Calculate tip amount based on the given percentage
    tip_amount = bill * (tip_percentage / 100)
    
    # Add tip to the original bill to get the final amount
    total_bill = bill + tip_amount
    
    # Divide total bill among all people
    per_person = total_bill / people

    # Return all calculated values
    return tip_amount, total_bill, per_person


try:
    # Taking user input for bill amount
    bill = float(input("Enter total bill amount: "))

    # Taking user input for tip percentage
    tip_percentage = float(input("Enter tip percentage: "))

    # Taking number of people splitting the bill
    people = int(input("Enter number of people splitting: "))


    # Checking if entered values are valid
    if bill <= 0 or tip_percentage < 0 or people <= 0:
        print("Please enter valid positive values.")

    else:
        # Calling the function to perform calculations
        tip, total, individual = calculate_bill(
            bill,
            tip_percentage,
            people
        )

        # Displaying final bill details in a formatted way
        print("\n----- Bill Summary -----")
        print(f"Tip Amount: ${tip:.2f}")
        print(f"Total Bill: ${total:.2f}")
        print(f"Each Person Pays: ${individual:.2f}")


# Handling errors if user enters incorrect data type
except ValueError:
    print("Invalid input. Please enter numbers only.")