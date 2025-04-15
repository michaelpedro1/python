try:
    num1, num2=eval(input('enter two numers separeted by a comma'))
    result=num1/num2
    print('result is', result)
except ZeroDivisionError:
    print('division by zero error')
except SyntaxError:
    print('add a comma between the two values.')

else:
    print('no exceptions')
finally:
    print('happy caculations')                