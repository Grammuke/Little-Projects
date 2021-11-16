while True:
    print('1 Addition')
    print('2 Subtraction')
    print('3 Multiplication')
    print('4 Division')
    print('5 Exit')
    choice = input('Enter your choice:')
    if 1<=int(choice)<=4:
        number1 = int(input('Enter 1st number:'))
        number2 = int(input('Enter 1st number:'))
        if int(choice)==1:
            print('Addition is:', eval('number1+number2'))
        if int(choice) ==2:
            print('Subtraction is:', eval('number1-number2'))
        if int(choice) ==3:
            print('Multiplication is:', eval('number1*number2'))
        if int(choice) ==4:
            print('Division is:', eval('number1/number2'))
    if int(choice)==5:
        exit()
    else:
        print('Enter correct details')

