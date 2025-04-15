import random

playing=True
number=random.randint(0, 9)
print('i will gearate a random number between 0, 9. and you give your random number') 
while playing:
    guess=int(input('enter the number'))
    if guess == number:
        print('you wi the game. the number was', number)
        break
    else:
        print('please try again. the genarated number is')
