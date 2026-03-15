# DAY 2 : HOTEL BILL CALCULATOR PROJECT
print("Welcome to the hotel mathematical operator")
bill = float(input("What is the total bill? $"))
answer = input("Do you want to split the bill? (yes/no)? ")
if answer == "yes":
    member = int(input("How many members are you there to split the bill? $"))
    member = int(member)
    total = bill / member
    print("The each person should pay $" + str(total))
    print("Thank you for coming! and visit again")
elif answer == "no":
    print("the bill is to be paid: " + str(bill))
    print("Thank you for coming! and visit again")