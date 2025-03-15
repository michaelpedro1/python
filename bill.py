units=int (input('enter the number of units') )
cost=0
tax=25
if units<50:
    cost=units*2.60
    tax=25
elif units<100:
    cost=(50*2.60)=((units-50)*3.25)
    tax=35
elif units<200:
    cost=(50*2.60)+(50*3.25)+((units-100)*5.26)
    tax=45
else:
    cost=(50*2.60)+(50*3.25)+(+100*5.26)+((units-200)*8.45)
    tax=75
amount=cost-tax
print('bill is',amount)                
