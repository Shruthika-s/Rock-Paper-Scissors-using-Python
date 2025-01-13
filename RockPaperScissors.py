rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

print("Welcome to the rock paper scissors game.")
choice = int(
    input(
        "What do you choose? Type 0 for rock, 1 for paper or 2 for scissors. \n"
    ))
if choice == 0:
    print(rock)
elif choice == 1:
    print(paper)
elif choice == 2:
    print(scissors)

comp_choice = random.randint(0, 2)
print("Computer chose: ")
if comp_choice == 0:
    print(rock)
elif comp_choice == 1:
    print(paper)
elif comp_choice == 2:
    print(scissors)

if choice >= 3 or choice < 0:
    print("You typed an invalid number, you lose!")
elif choice == 0 and comp_choice == 2:
    print("You win!")
elif comp_choice == 0 and choice == 2:
    print("You lose")
elif comp_choice > choice:
    print("You lose")
elif choice > choice:
    print("You win!")
elif comp_choice == choice:
    print("It's a draw")