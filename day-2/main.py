print("Welcome to the tip calculator!")
bill = float(input("What's the total bill?\n"))
tip = int(input("How much tip would you like to give?\n"))
people = int(input("How many people to split the bill?\n"))
bill_with_tip = tip / 100 * bill + bill
print(f"Each person should pay: ${bill_with_tip / people}")
