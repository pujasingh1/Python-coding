print("Welcome to the tip calculator")

bill = float(input("What was the total bill? Rs"))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))

tip_as_percent = tip/100
bill_as_percent = bill * tip_as_percent
total_bill = bill + bill_as_percent
bill_per_person = total_bill / people
bill_with_tip = tip/100 * bill + bill

final_bill = (f"Each person should pay: Rs",round(bill_per_person, 2))
print(Final_bill)
