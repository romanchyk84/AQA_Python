# Четверта домашка. https://github.com/romanchyk84/AQA_Python.git
print('\n---Перша задача---')
# 1 - Є 3 группи людей(sets) australia_blacklist, poker_blacklist, alcohol_blacklist. \
# В кожній групі вказані імена. Вивести тих хто виграв джекпот(є одразу в 3х списках)

australia_blacklist = {'Alex', 'Joe', 'Mary', 'Vova','Jason', 'Viktor', 'Helen'}
poker_blacklist = {'Mary', 'Linda', 'John', 'Olha', 'Jason', 'Helen', 'Iryna'}
alcohol_blacklist = {'Steven', 'Helen', 'Mary', 'Nick', 'Jack', 'Jason', 'Maryna'}

names = australia_blacklist.intersection(poker_blacklist).intersection(alcohol_blacklist)
dif_names = names.symmetric_difference(australia_blacklist).symmetric_difference(poker_blacklist).symmetric_difference(alcohol_blacklist)
print(f'Джекпот виграли {len(names)} учасники: {", ".join(names)}!')
print(f'Усім іншим {len(dif_names)} учасникам цього разу не пощастило. Бажаємо: {", ".join(dif_names)} успіхів наступного разу.')
# End

print('\n---Наступна задача---')
# 2 - Словник має наступні дані: {'Alex': 'house', 'Max': 'Flat', 'Olha': 'Appartments', 'Oleh': 'Trench'}
# Використвоючі f-string вивести: "User_name is living in place_name" для кожного юзера. Використовувати цикл

pers_data = {
    'Alex': 'house',
    'Max': 'Flat',
    'Olha': 'Appartments',
    'Oleh': 'Trench'
}

for key in pers_data:
    print(f'"{key} is living in {pers_data[key]}"')
# End

print('\n---Наступна задача---')
# 3 - Є список ['Jack', 'Leon', 'Alice', None, 32, 'Bob']
# Вивести ТІЛЬКИ коректні імена(тобто стрінги). Використовувати Continue.

names_list = ['Jack', 'Leon', 'Alice', None, 32, 'Bob']
a = []
# b = []
for name in names_list:
    if isinstance(name, str):
        a.append(name)
        continue
    # else:
    #     b.append(name)
print(f'Такі імена як {", ".join(a)} є коректними.')
# print(f'-------- не є стрінгою {b} --------')
# End


print('\n---Наступна задача---')
# else:
#     print('done')


# for el in pers_data:
#     print(el)
# else:
#     print('done')


# matrix = [
#     australia_blacklist,
#     poker_blacklist,
#     alcohol_blacklist
# ]
#
# for row in matrix:
#     print(row)
#     for name in row:
#         print(name)

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
# ]
#
# for row in matrix:
#     print(row)
#     if 3 in row:
#         continue
#
#     for number in row:
#         print(number)
#         if number in (2, 5, 8):
#             break