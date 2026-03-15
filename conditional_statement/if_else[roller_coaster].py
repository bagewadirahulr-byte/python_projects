# [ROLLER COASTER]
print("WELCOME TO THEME PARK")
answer = input("WANNA RIDE ROLLERCOASTER? (yes/no)")
print("NOTE:- TO RIDE ROLLERCOASTER YOUR HEIGHT MUST 120CM+ ")
if answer == "yes":
    height = float(input("\nWHAT IS YOUR HEIGHT? "))
    if height >= 120 :
        height = int(height)
        print(f"YOUR HEIGHT IS {height} HENCE, YOU CAN ENJOY THE RIDE")
    else:
        print(f"SORRY! YOUR HEIGHT IS {height} HENCE, YOU CAN'T RIDE")
else:
    print("FINE! YOU CAN ENJOY THE OTHER GAMES IN THIS THEME PARK")