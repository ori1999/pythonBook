languages = ['python','c++','c','java']
print(languages)

languages[0] = 'php'
print(languages)

languages[0] = 'python'
print(languages)

languages.pop()
print(languages)


del languages[1]
print(languages)

languages.insert(0,'js')
print(languages)

languages.append('kotlin')
print(languages)

#sort永久排序
languages.sort()
print(languages)

languages.sort(reverse=True)
print(languages)

#sorted临时排序
sorted(languages)
print(languages)
print(sorted(languages))

sorted(languages,reverse=True)
print(languages)
print(sorted(languages,reverse=True))

