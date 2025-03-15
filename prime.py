lower=int(input('enter the lowest range'))
upper=int(input('enter the upper range'))
print('the prime numers between',lower,'and', upper)
for num in range(lower, upper+1):
    if num>1:
        for x in range(2, num):
            if (num%x==0):
                break
        else:
            print(num)    
