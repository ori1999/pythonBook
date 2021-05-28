names = ['admin','b','c','d','e']
for name in names:
    if name == 'admin':
        print(f'hello,{name}')
    else:
        print(f'hello,{name},thank you')

if names == []:
    print('we need to find some users')
del names[:]
if names == []:
    print('we need to find some users')