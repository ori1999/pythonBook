while True:
    age = int(input('your age:'))
    if age < 3:
        print('0')
    elif age >= 3 and age < 12:
        print('10')
    else:
        print('15')