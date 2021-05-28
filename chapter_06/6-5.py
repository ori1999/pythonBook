rivers = {
    'a':'j',
    'b':'k',
    'c':'l',
}
for key,value in rivers.items():
    print(f'the {value} runs through {key}')
for key in rivers:
    print(f'{key}')
for key in rivers:
    print(f'{rivers[key]}')