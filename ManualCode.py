# Tip & Split Calculator

bill = float(input("Enter total bill amount: "))
tip_percent = float(input("Enter tip percentage : "))
people = int(input("Enter number of people splitting: "))

tip_amount = bill * (tip_percent / 100)
total_bill = bill + tip_amount
per_person = total_bill / people

print("Total Tip: $" + str(round(tip_amount, 2)))
print("Total Bill: $" + str(round(total_bill, 2)))
print("Each person pays: $" + str(round(per_person, 2)))