def add(x, y):
    return x+y
def subbtract(x, y):
    return x-y
def multip(x, y):
    return x*y
def divide(x, y):
    return x/y   
print('select the operation')
print('a.  +')
print('b.  -')
print('c.  /')
print('d.  *')
option=input('give your option(a,b,c,d)')
num1=int(input('enter th first number'))
num2=int(input('enter the second number'))
if option == 'a':
    print(num1,'+', num2 , '=', add(num1, num2))
elif option == 'b':
    print(num1,'-', num2 , '=', subbtract(num1, num2))
elif option == 'c':
    print(num1,'/', num2 , '=', divide(num1, num2))
elif option == 'd':
    print(num1,'*', num2 , '=', multip(num1, num2))        