 # stone paper scissor
import random
import pyfiglet

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)     ROCK '''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)     PAPER'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)       SCISSORS'''

game_images =[rock, paper, scissors]
user_choice = int(input("what do you chose? Type 0 for rock, Type 1 for paper and Type 2 for scissors\n "))
if user_choice >=0 and user_choice <=2:
    print(game_images[user_choice])
computer_choice = random.randint(0, 2)
print("computer chose : ")
print(game_images[computer_choice])
if user_choice >=3 or user_choice <0:
    print(pyfiglet.figlet_format("invalid      input !"))
elif user_choice == computer_choice :
    print(pyfiglet.figlet_format("     draw"))
elif  user_choice ==0 and computer_choice ==2:
    print(pyfiglet.figlet_format("    you win"))
elif user_choice ==2 and computer_choice ==0:
    print(pyfiglet.figlet_format("      you lose"))
elif user_choice > computer_choice:
    print(pyfiglet.figlet_format("       you win"))
elif user_choice < computer_choice:
    print(pyfiglet.figlet_format("      you lose"))


