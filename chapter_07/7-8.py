sandwich_orders = ['a','b','c']
finished_sandwiches = []
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f'i made your {current_sandwich} sandwich.')
    finished_sandwiches.append(current_sandwich)
print(finished_sandwiches)