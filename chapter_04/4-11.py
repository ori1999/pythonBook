pizzas = ['a','b','c']
for pizza in pizzas:
    print(pizza)
    print(f'i like {pizza} pizza.')
print('i really like pizza.')

friend_pizzas = pizzas[:]#添加[:]后，是将后者的副本赋值给前者，两个列表不关联，这里的切片是从第一个元素到最后一个元素
copy_pizzas = pizzas#如果不添加[:]，两个列表相关联；

pizzas.append('d')
friend_pizzas.append('e')
print(f'my favorite pizzas are:{pizzas}')
print(f"my friend's favorite pizzas are:{friend_pizzas}")
copy_pizzas.append('f')
print(f'my favorite pizzas are:{pizzas}')
print(f'copy pizzas are:{copy_pizzas}')