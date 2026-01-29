import random

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
choice_1 = [rock,paper,scissors]
computer_choice = random.randint(0,2)
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
print(choice_1[user_choice])
print("Computer chose:")
print(choice_1[computer_choice])

if user_choice == 0 and computer_choice == 2:
    print("You Win")
elif user_choice == 2 and computer_choice == 1:
    print("You Win")
elif user_choice == 1 and computer_choice == 0:
    print("You win")
elif user_choice == 2 and computer_choice == 0:
    print("lose")
elif user_choice == 1 and computer_choice == 2:
    print("lose")
elif user_choice == 0 and computer_choice == 1:
    print("lose")
else:
    print("Tie")