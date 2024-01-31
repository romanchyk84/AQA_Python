# # # Список преобразовать в словарь в квадрате
# str_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
#
# dict2 = dict(map(lambda x: (int(x), int(x)**2), str_list))
# print(dict2)

# from copy import deepcopy
#
# list1 = [1, 2, 3, 4, 5, 6, {1: 2, 2: 5}, 'z', 'y']
# prod1 = list1
# list2 = deepcopy(list1)
# list1[6][1] = 9
# list2.append('w')
# print(id(list1[6]), list1[6])
# print(id(list2[6]), list2[6])