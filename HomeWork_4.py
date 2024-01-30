# Четверта домашка. https://github.com/romanchyk84/AQA_Python.git
"""1 - Є 3 группи людей(sets) australia_blacklist, poker_blacklist, alcohol_blacklist. \
В кожній групі вказані імена. Вивести тих хто виграв джекпот(є одразу в 3х списках)"""

australia_blacklist = {'Alex', 'Joe', 'Mary', 'Vova','Jason', 'Viktor', 'Helen'}
poker_blacklist = {'Mary', 'Linda', 'John', 'Olha', 'Jason', 'Helen', 'Iryna'}
alcohol_blacklist = {'Steven', 'Helen', 'Mary', 'Nick', 'Jack', 'Jason', 'Maryna'}

names = australia_blacklist.intersection(poker_blacklist).intersection(alcohol_blacklist)
print(f'Джекпот виграли {len(names)} учасники: {", ".join(names)}!')


"""2 - Словник має наступні дані: {'Alex': 'house', 'Max': 'Flat', 'Olha': 'Appartments', 'Oleh': 'Trench'}
Використвоючі f-string вивести: "User_name is living in place_name" для кожного юзера. Використовувати цикл"""