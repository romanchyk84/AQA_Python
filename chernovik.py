# tekst = input('Vvedite vash tekst: ')
#
# letters = {}
#
# for word in tekst:
#     if word.isalpha():
#         word= word.upper()
#         letters[word] = letters.get(word, 0) +1
#
#
# for key in letters:
#     print(f'Літера "{key}" використовується - {letters[key]} раз(-а, -ів)')

# from copy import deepcopy
#
# # Разница между deepcopy и copy
# first_list = [1, 2, 3, 4, {'name': 'Roman', 'age': 39, 'city': 'Chisinau'}, 5]
# second_list = deepcopy(first_list)
# third_list = first_list.copy()
#
# Добавление элемента в список
# first_list.append(6)
# first_list[4][0]=0
# second_list[4]['country'] = 'Moldova'
# # second_list.append([4],['country'] = 'RM')
# print(id(first_list),first_list)
# print(id(second_list),second_list)
# print(id(third_list),third_list)
#
#
# third_list[4][2]=1
# print(third_list)
# print(first_list)
# Удаление элемента из вложенного словаря
# deldict3 = third_list[4]
# del deldict3[2]
#
# deldict1 = first_list[4]
# del deldict1[0]
# first_list.remove(5)
#
# deldict2 = second_list[4]
# del deldict2['age']
#
# print('\n',third_list)
# print(first_list)
# print(second_list)