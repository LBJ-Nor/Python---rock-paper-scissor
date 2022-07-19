import random

print("""WELCOME WELCOME, This is rock, paper, scissors please select a letter to play!
type help for input options""")
choices = ["R", "P", "S"]
w_outcome = ["RS", "PR", "SP"]
player_score = 0
npc_score = 0
help_text = """
R - Rock
P - Paper
S - Scissors
type quit to end
"""


while True:

    player_choice = input("R, P, S?: ").upper()
    npc_choice = (random.choice(choices))

    if player_choice == "HELP":
        print(help_text)
        
    elif player_choice == "QUIT":
        print("Thank you for playing.")
        break
    
    elif player_choice not in choices:
        print("Please enter R, P, or S for Rock, Paper or Scissor")

    else:
        print("You chose:", player_choice, "Computer chose:", npc_choice)
        
        if player_choice + npc_choice in w_outcome:
            player_score += 1
            print("You win")
        if npc_choice == player_choice:
            print("It`s a draw")
        if npc_choice + player_choice in w_outcome:
            npc_score += 1
            print("You lose")

        print("Player score:", player_score, "NPC score:", npc_score)
