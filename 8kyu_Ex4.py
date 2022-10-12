# Ваша задача состоит в том, чтобы создать функцию, которая может 
# принимать любое неотрицательное целое число в качестве аргумента 
# и возвращать его с цифрами в порядке убывания. 
# Вход: 42145 Выход: 54421

test_string = 42145
test_string = str(test_string)
test_string = list(test_string)
max_el = max(test_string)

result_string = ''
for i in range(len(test_string)):
    for j in range(len(test_string)):
        if test_string[j] == max(test_string):
            result_string += test_string[j]
            del test_string[j]
            break
result_string = int(result_string)
print(result_string)

# сортировка от большего к меньшему методом

test_string = '42145'
test_string = list(test_string)
test_string.sort(reverse = True)
print(''.join(test_string))
