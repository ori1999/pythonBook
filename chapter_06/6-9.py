favorite_places  = {
    'a':['q','w','e'],
    'b':['r'],
    'c':['t','y'],
}
for key,values in favorite_places.items():
    print(f'{key}-')
    for value in values:
        print(f'{value}')
    print('-----------')