# Сколько овец в списке(True)

array1 = [True,  True,  True,  False,
          True,  True,  True,  True ,
          True,  False, True,  False,
          True,  False, False, True ,
          True,  True,  True,  True ,
          False, False, True,  True ]

def count_sheeps(list):
    list2 = []
    for i in range(len(list)):
        if list[i] == True:
            list2.append(list[i])
    result = len(list2)
    return result
print(count_sheeps(array1))

result = lambda list1: [list1[i] for i in range(len(list1)) if list1[i] == True]
print(len(list(result(array1))))

