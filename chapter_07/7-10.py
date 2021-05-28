name_s = 'your name:'
place_s = 'wanted place:'
isContinue = 'continue?(yes/no):'
dict = {}
while True:
    name = input(name_s)
    wanted_place = input(place_s)
    dict[name] = wanted_place
    for key,value in dict.items():
        print(f'{key}:{value}')
    continue_or_not = input(isContinue)
    if continue_or_not == 'yes':
        continue
    else:
        break
for key,value in dict.items():
    print(f'{key}:{value}')