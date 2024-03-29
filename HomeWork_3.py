# HomeWork_3 on Gitgub https://github.com/romanchyk84/AQA_Python.git

# 1) Запропонувати юзеру створити список(введіть продукти через пробіл)
purchase = input("\tВведите список продуктов через пробел: ")

# 2) Строку яку ввів юзер перевести в список
purchase_spisok = purchase.split()

# 3)Надрукувати список який ввів юзер
print(f'\tВаш список состоит из {len(purchase_spisok)} элемента(-ов): {", ".join(purchase_spisok)}')
print('-----------------------------------')
print(f'Айдишник списка: {id(purchase_spisok)}, элементов в списке: {len(purchase_spisok)}, класс: {type(purchase_spisok)}')
print('-----------------------------------')

# 4) Якщо юзер нічогоне ввів(або ввів лише пробіли) то написати список продуктів порожній і закінчити програму
# 5) Запропонувати юзеру ввести продукт та ознаку чи варто його видаляти чи додавати(якщо видаляти, то продукт починаеться з -
# 6) Додати/видалити продукт
# 7) Надрукувати оновлений список продуктів
# 8) Продовжувати поки список не стане порожнім
while len(purchase_spisok) != 0:
    new_purchase = input("\n\tЖелаете добавить или удалить (для удаления перед элементом поставьте знак '-') продукт из списка?: ")

    if new_purchase.startswith('-'):
        for_del = new_purchase.split('-')[1]
        if for_del in purchase_spisok:
            purchase_spisok.remove(for_del)
        else:
            print("\n\t-=-=- Такого продукта нет в списке! -=-=-")

    elif new_purchase.startswith(''):
        purchase_spisok.append(new_purchase)
    print(f'\n\tВ вашем списке {len(purchase_spisok)} продукта(-ов): {", ".join(purchase_spisok)}')

else:
    print('\nВсе продукты удалены или не добавлены. На данный момент ваш список пуст.')
