height=float(input('Enter the height in cm'))
weight=float(input('Enter the weight in kg'))
BMI=weight/(height/100)**2
if BMI<18.5: 
    print (BMI, 'You are underweight')
elif BMI<25.5: 
    print (BMI, 'You are healthy')
elif BMI<30.5:
    print(BMI, 'you are overweight')
else: 
    print('You are obese' )
