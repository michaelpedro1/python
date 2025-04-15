repeat=False
while not repeat:
    try:
        n=int(input('give a number'))
        while n%4==0:
            print('this will repeat')
        repeat= True
    except ValueError:
        print('invalid value')
                
