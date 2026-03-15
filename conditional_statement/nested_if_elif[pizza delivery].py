print("welcome to python pizza delivery")
size = input("what size pizza do you want? s, m or l: ")
pepperoni = input("do you prefer pepperoni on pizza?(y/n): ")
extra_cheese = input("do you prefer extra_cheese on pizza?(yes/no) ")
bill = 0
if size == "s":
    bill += 15
elif size == "m":
    bill += 20
elif size == "l":
    bill += 25
else:
    print("you have entered wrong inputs")
if pepperoni == "y":
    if size == "s":
        bill += 2
    else:
        bill += 3
if extra_cheese == "y":
    bill += 1
else:
    print(f"total bill is ${bill}")