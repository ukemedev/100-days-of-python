import random

rock = """
_______
---'   )
    ()
     ()
      ()
---.(_)
"""

paper = """
_______
---'    )
______)
      ____)
          )
---.)
"""

scissors = """
_______
---'   )
    _)
______)
    ()
---.()
"""

print("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors")

game_choice = [rock, paper, scissors]

users_choice = int(input())
computer_choice = random.randint(0, 2)

if users_choice == 0 and computer_choice == 2:
    print(game_choice[users_choice])
    print(game_choice[computer_choice])
    print("you won!")
elif users_choice == 2 and computer_choice == 1:
    print(game_choice[users_choice])
    print(game_choice[computer_choice])
    print("you won!")
elif users_choice == 1 and computer_choice == 0:
    print(game_choice[users_choice])
    print(game_choice[computer_choice])
    print("you won!")
elif users_choice == computer_choice:
    print(game_choice[users_choice])
    print(game_choice[computer_choice])
    print("it's a draw!")
else:
    print(game_choice[users_choice])
    print(game_choice[computer_choice])
    print("you lose!")
