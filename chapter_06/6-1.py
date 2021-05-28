friend = {
    'first_name':'zhang',
    'last_name':'ming',
    'age':'12',
    'city':'beijing'
}
# print(friend['first_name'])
# print(friend['last_name'])
# print(friend['age'])
# print(friend['city'])
for key in friend:
    print(f'{key}:{friend[key]}')