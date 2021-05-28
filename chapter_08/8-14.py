def make_car(company, model, **info):
    info[company] = company
    info[model] = model
    return info


car = make_car('subaru', 'outback', color='red', two_package=True)
print(car)
