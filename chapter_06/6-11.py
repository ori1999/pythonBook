cities = {
    'beijing':{
        'country':'china',
        'population':77889911,
        'fact':'one'
    },
    'shanghai':{
        'country':'china',
        'population':12345671,
        'fact':'two'
    },
    'chongqing':{
        'country':'china',
        'population':33225544,
        'fact':'three'
    }
}
for city,info in cities.items():
    print(f'=={city}')
    for key,value in info.items():
        print(f'>>{key}--{value}')
    print()