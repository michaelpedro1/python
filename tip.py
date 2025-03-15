def total(bill, tip):
    total=bill*(0.01*tip)
    total=round(total, 2)
    print('your total amount is', total)
total(700, 40)

def sum():
    x=10
    y=20
    print(x+y)
sum()    
 

def cube(a):
    return a*a*a
print(cube(10))

def bytwo(y):
    if y%2==0:
        print(y, 'is  divisible y 2')
    else:
        print(y, 'is not divisible by 2 ')
bytwo(10) 

def factorial(u):
    if u==0 or u==1:
        return 1
    else:
        return u*factorial(u-1)
print(factorial(5))    
