current_users = ['admin', 'B', 'c', 'd', 'e']
new_users = ['d', 'e', 'f', 'g', 'h', 'b']
# for new_user in new_users:
#     if new_user in current_users:
#         print('you need an other name.')
#     else:
#         print('this name has not used.')


# 确保不区分大小写
current_users_lower = [current_user.lower() for current_user in current_users]
print(current_users_lower)
for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f'{new_user},you need an other name.')
    else:
        print(f'{new_user},this name has not used.')
