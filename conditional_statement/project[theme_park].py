# THEME PARK PROJECT [created by me]
print("Welcome to the theme park ")
ticket = int(input("How many tickets do you want? "))
if ticket >1:
    adult_age = int(input("How many are above age of 18? "))
    print("NOTE:- THE PRICE FOR ABOVE AGE OF 18 IS '$12' ")
    if ticket < adult_age :
        print("you forgot to buy extra ticket/tickets so rerun the code!")
    else :
        price_for_adult_age = int(12)
        bill_for_adult_age = adult_age * price_for_adult_age
        below_age = int(input("How many are below and age of 18? "))
        print("NOTE:- THE PRICE FOR BELOW AGE OF 18 IS '$7' ")
        if adult_age + below_age > ticket or adult_age + below_age < ticket :
            print("you have to buy extra ticket/tickets!\n'or'\nyour buying extra ticket/tickets!\n SO RERUN THE CODE!")
        else :
            price_for_below_age = int(7)
            bill_for_below_age = below_age * price_for_below_age
            print(f"\nthe bill of above 18 age= ${bill_for_adult_age}")
            print(f"the bill of below and age of 18= ${bill_for_below_age}")
            total_bill = int(bill_for_adult_age + bill_for_below_age)
            print(f"the total bill = ${total_bill}")
            print("PAY IT! AND  ENJOY THE DAY!")
elif ticket == 1:
    answer = input("are you above the age of 18?(yes/no): ")
    if answer == "yes":
        print("you have to pay $12 for the ticket")
    else:
        print("you have to pay $7 for the ticket")