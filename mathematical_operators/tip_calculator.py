#  TIP CALCULATOR
print("Welcome to the tip mathematical operator")
bill = float(input("What was the total bill? $"))
tip = float(input("What percentage tip would you like to give? "))
member = int(input("How many members to split the bill? "))
tip = int(tip)
tip_percent = tip / 100
member = int(member)
total = (bill * tip_percent + bill) / member
total = round(total, 2)
print(f"Each member should pay: ${total}")