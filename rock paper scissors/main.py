import random
while True:
    choices=['rock','paper','scissors']
    player=None

    computer =random.choice(choices)
    while player not in choices:
        player=input("rock,paper or sciddors: ").lower()

    if player==computer:
        print('Computer: ',computer)
        print('player: ',player)
        print('Tie')
    elif player=='rock':
        if computer=="paper":
            print("computer: ",computer)
            print("player: ",player)
            print('you lose')
        if computer=="scissors":
            print("computer: ",computer)
            print("player: ",player)
            print('you win')
    elif player=='scissors':
        if computer=="rock":
            print("computer: ",computer)
            print("player: ",player)
            print('you lose')
        if computer=="paper":
            print("computer: ",computer)
            print("player: ",player)
            print('you win')
    elif player=='paper':
        if computer=="scissors":
            print("computer: ",computer)
            print("player: ",player)
            print('you lose')
        if computer=="rock":
            print("computer: ",computer)
            print("player: ",player)
            print('you win')

    play_again=input("Play again? (yes/no): ").lower()

    if play_again !="yes":
        break
print("Bye!")
