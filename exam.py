medical_cause=input('did you have a medical cause: y or N')
attendance=int(input('give your attendance pecentage'))
if medical_cause =='y':
    print('you can do the exam')
else:
    if attendance>75:
        print('you can do the exam')
    else:
        print('ot allowed')
                