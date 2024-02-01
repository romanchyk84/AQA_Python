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

print('\n---Друга задача---')
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

print('\n---Третя задача---')
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
print(f'Такі імена як {", ".join(a)} є коректними, тобто є стрінгою.')
# print(f'-------- не є стрінгою {b} --------')
# End


print('\n---Четверта задача---')
# 4 - Порахувати та вивести(print) кількість букв в строці.
# Юзер щось вводить(input)
# Ваша задача надрукувати кількість кожного символу того що він ввів.
# Прикдад:
# Юзер вводить:
# My name is Emmy Santiago.
# ВИ прінтаете щось накшталт:
# M = 1, y = 2, n = 2, ...(або в іншому форматі, це не принциповоб головне, що б чітко було зрозуміло скільки разів зустрічаеться кожна буква)
# Тобто кожну букву та скільки разів вона зустрічаеться
# Підказка: це про словники, get можна використати для тотго щоб витягнути чи є ключ без помилки та надати дефолтне значення

tekst = input('Введіть ваш текст: ')

letters = {}

for word in tekst:
    if word.isalpha():
        word = word.upper()
        letters[word] = letters.get(word, 0) +1
    elif word.isdigit():
        letters[word] = letters.get(word, 0) + 1

for key in letters:
    print(f'Літера "{key}" використовується - {letters[key]} раз(-а, -ів)')
# End


print('\n---Задача без оцінювання---')
# Ви створюєте список в якому може бути None(а може і не бути)
# Мета: надрукувати "There is no None" у випадку якщо None не зустрічаеться у списку
# Умови:
# По списку ми йдемо циклом
# Не створювати змінні(крім списку про який сказано вище)
# використати if 1 раз
# # Не використовувати методи/функції/класи

smtn = [1,  2, True, 'a', 'none', None, 'b', 123]
print(smtn)

for el in smtn:
    if el is None:
        print('NONE is here')
        break

else:
    print('There is no NONE')
# End

