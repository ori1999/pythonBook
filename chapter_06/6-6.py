favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

# friends = ['phil', 'sarah']
# for name in favorite_languages.keys():
#     print(name.title())
#
#     if name in friends:
#         language = favorite_languages[name].title()
#         print(f"\t{name.title()}, I see you love {language}!")

news = ['jen','a','b','sarah']

for key in favorite_languages:
    if key in news:
        print(f'thank you,{key}')
    else:
        print(f'welcome,{key}')