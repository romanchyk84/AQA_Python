# Список преобразовать в словарь в квадрате
str_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

dict2 = dict(map(lambda x: (int(x), int(x)**2), str_list))
print(dict2)

bkn