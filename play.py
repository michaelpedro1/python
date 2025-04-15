L=[2,6,8,4,1,5]
print(L)
sum=0
for i in L:
    sum=sum+i
count=len(L)
avg=sum/count
print(sum)
print(avg)
L.sort()
print(L[0])
print(L[5]) 