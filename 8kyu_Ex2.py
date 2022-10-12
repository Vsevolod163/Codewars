from cgitb import reset

# на вход приходит число и размер массива, вывести список первых элементов кратных числу

def county(x, size):
    result = []
    for i in range(0, size * x, x):
        result.append(x + i)
    return result
print(county(3, 5))


result = lambda x, size: [x + i for i in range(0, size * x, x)]
print(list(result(3, 5)))
