def armstrong (m):
    numstring=str(m)
    digits=len(numstring)

    sums=sum(int(digit)**digits for digit in numstring)
    return sums == m
m=int(input('enter the number to check'))
if armstrong(m):
    print(m, 's armstrong')
else:
    print(m, 'not armstrong')    