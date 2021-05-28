sandwich_orders = ['a','b','c','a','a']
finished_sandwich = []
print('a is soided over.')
#遍历列表里的'a'并从列表中删除
while 'a' in sandwich_orders:
    sandwich_orders.remove('a')
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(current_sandwich)
    finished_sandwich.append(current_sandwich)
print(finished_sandwich)