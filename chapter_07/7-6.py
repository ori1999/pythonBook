# while True:
#     pizza = input('Enter:')
#     if pizza == 'quit':
#         break
#     else:
#         print(f'ok,we will take {pizza}')


# active = True
# while active:
#     pizza = input('Enter:')
#     if pizza == 'quit':
#         active = False
#     else:
#         print(f'ok,we will take {pizza}')


# while True:
#     age = int(input('your age:'))
#     if age < 3 and age > 0:
#         print('0')
#     elif age >= 3 and age < 12:
#         print('10')
#     elif age >= 12:
#         print('15')
#     elif age == 0:
#         break

# active = True
# while active:
#     age = int(input('your age:'))
#     if age < 3 and age > 0:
#         print('0')
#     elif age >= 3 and age < 12:
#         print('10')
#     elif age >= 12:
#         print('15')
#     elif age == 0:
#         active = False


while True:
    q = input('your age:')
    if q == 'quit':
        break
    age = int(q)
    if age < 3 and age > 0:
        print('0')
    elif age >= 3 and age < 12:
        print('10')
    else:
        print('15')