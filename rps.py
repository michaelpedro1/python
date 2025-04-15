import random
while True:
    userchoice=input('enter your choice: rock , paper and scissors')
    possiblereactions=['rock', 'paper', 'scissors']
    if userchoice not in possiblereactions:
        print('invalid choice. try again')
        continue
    computerchoice=random.choice(possiblereactions)
    print('your choice is', userchoice, 'the computer choice is', computerchoice )
    if userchoice == computerchoice:
        print('its a tie. the choice is ', userchoice)
    elif userchoice == 'rock':
        if computerchoice == 'scissors':
            print('rock smashes')    