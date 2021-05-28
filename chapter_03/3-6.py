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