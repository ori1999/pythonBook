nums = {
    'a':[1,6,5],
    'b':[2,5],
    'c':[7,6,4],
    'd':[12,22,55],
    'e':[31,21,35]
}
for name,num in nums.items():
    print(f'==name')
    for i in num:
        print(f'>>{i}')
    print('-----------')