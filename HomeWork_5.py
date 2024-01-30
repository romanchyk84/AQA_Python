# # Список преобразовать в словарь в квадрате
# str_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
#
# dict2 = dict(map(lambda x: (int(x), int(x)**2), str_list))
# print(dict2)


# 1) Запропонувати юзеру створити список(введіть продукти через пробіл)
purchase = input("Введите список продуктов через пробел: ")

# 2) Строку яку ввів юзер перевести в список
purchase_spisok = purchase.split()

# 3)Надрукувати список який ввів юзер
print(purchase_spisok)
print(len(purchase_spisok))
# 4) Якщо юзер нічогоне ввів(або ввів лише пробіли) то написати список продуктів порожній і закінчити програму

new_purchase = input("Хотите добавить или удалить продукт из списка?: ")

# if new_purchase.startswith(''):
#     purchase_spisok.append(new_purchase)

while len(purchase_spisok) == 0:

    if new_purchase.startswith('-'):
        for_del = new_purchase.split('-')[1]
        if for_del in purchase_spisok:
            purchase_spisok.remove(for_del)
        else:
            print("Такого продукта нет в списке")
    print(id(purchase_spisok),len(purchase_spisok), purchase_spisok)

else:
    print(len(purchase_spisok), purchase_spisok, 'Список пуст')