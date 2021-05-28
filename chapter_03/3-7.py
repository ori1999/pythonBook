friend_names = ['letme','mlxg','xiaohu','ming','uzi']
for friend_name in friend_names:
    print(f'lets have a dinner together,{friend_name}.')
print(f'{friend_names[0]} cant come here')
friend_names[0] = 'gala'
print(f'lets have a dinner together,{friend_names[0]}.')
print(f'i find a bigger table.')
friend_names.insert(0,'zitai')
friend_names.insert(3,'karsa')
friend_names.append('jackeylove')
for friend_name in friend_names:
    print(f'lets have a dinner together,{friend_name}.')
print(friend_names)
print('i can only invite two friends.')
while True:
    if len(friend_names) > 2:
        print(f'sorry,i cant invite you,{friend_names[-1]}')
        friend_names.pop()
    else:
        break
for friend_name in friend_names:
    print(f'lets have a dinner together,{friend_name}.')
del friend_names[0]
del friend_names[0]
print(f'{friend_names}')