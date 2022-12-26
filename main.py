import time
from random import randint
t = ['Rock', 'Paper', 'Scissor']
computer = t[randint(0,2)]
player = False
while player == False:
    player = input("Rock, Paper, Scissor?")
    if player == computer:
        print("Tie")
    elif player == 'Rock':
        if computer == "Paper":
            print("computer choses",computer)
            time.sleep(2)
            print("You Lose!", computer, 'converse', player)
        else:
            print("computer choses", computer)
            time.sleep(2)
            print("You Win!", player,"smashes", computer)
    elif player =='Paper':
        if computer == "Rock":
            print("computer choses",computer)
            time.sleep(2)
            print("You Lose!", computer, 'converse', player)
        else:
            print("computer choses", computer)
            time.sleep(2)
            print("You Win!", player,"smashes", computer)
    elif player =='Scissor':
        if computer == "Rock":
            print("computer choses",computer)
            time.sleep(2)
            print("You Lose!", computer, 'converse', player)
        else:
            print("computer choses", computer)
            time.sleep(2)
            print("You Win!", player,"smashes", computer)
    else:
        print("Something went wrong, Please choose Rock, Paper, Scissor")
    player = False
    computer=t[randint(0,2)]