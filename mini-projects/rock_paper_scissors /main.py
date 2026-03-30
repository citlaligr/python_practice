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

# Store options in a list
options = [rock, paper, scissors]

user_option = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))

if user_option < 0 or user_option > 2:
    print("Wrong input")
else:
    print("You chose:")
    print(options[user_option])

    computer_option = random.randint(0, 2)
    print("Computer chose:")
    print(options[computer_option])

    # Game logic
    if user_option == computer_option:
        print("It's a draw")
    elif (user_option == 0 and computer_option == 2) or \
         (user_option == 1 and computer_option == 0) or \
         (user_option == 2 and computer_option == 1):
        print("You win")
    else:
        print("You lose")
