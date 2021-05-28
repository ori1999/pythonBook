def make_album(singer_name, album_name, song_num=None):
    album_info = {}
    album_info['singer_name'] = singer_name
    album_info['album_name'] = album_name
    if song_num:
        album_info['song_num'] = song_num
    return album_info


# print(make_album('周杰伦','稻香'))
# print(make_album('凤凰传奇','月亮之上'))
# print(make_album('林俊杰','江南'))
# print(make_album('张国荣','当年情',12))
active = True
while active:
    user_singer_name = input('user_singer_name:')
    album_name = input('album_name:')
    song_num = input('song_num:')
    print(make_album(user_singer_name, album_name, song_num))
    isContinue = input('isContinue?(yes/no):')
    if isContinue == 'yes':
        continue
    else:
        break
