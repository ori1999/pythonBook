# 形参前面加*表示作为元组处理，**表示作为字典处理
def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


# user_profile = build_profile('albert', 'einstein',
#                              location='princeton',
#                              field='physics')
# print(user_profile)
my_profile = build_profile('li', 'shuai', country='China', city='shanghai')
print(my_profile)
