try:
    num=int(input('enter your age'))
    print('you are', num, 'years old')
except ValueError as ex:
    print('exceptio raised:', ex)    