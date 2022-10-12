# На вход приходит число, вывести сумму элементов от 1 до данного числа

def summation(num):
    
    return map(str, lambda num: [num + i for i in range(num + 1)])

print(summation(5))

res = lambda num: [i for i in range(num + 1)]
print((sum(list(res(5)))))

print(sum(range(6)))