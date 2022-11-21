import random

def play():
    player = input ("rock is 'r', paper is 'p', scissors is 's'" )
    computer = random.choice(['r', 'p', 's'])
    print(computer)

    if player == computer:
        return "Tie"
    if is_win(player, computer):
        return "you won"

    return "you lost"




def is_win(player, computer):
    if (player == 'r' and computer == 's') or (player == 'p' and computer == 'r') or (player == 's' and computer == 'p'):
        return True
print(play())

