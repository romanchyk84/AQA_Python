# # # Список преобразовать в словарь в квадрате
str_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

q1 = list(map(int, str_list))
q2 = list(map(lambda x: x ** 2, q1))

print(dict(zip(q1, q2)))
# End
print('__'*30)

"""
Напишіть інтерактивний калькулятор. Передбачається, що користувач вводить формулу, що складається з числа, оператора
(як мінімум * і /) та іншого числа, розділених пробілом (наприклад, 2 * 5).

Якщо вхідні дані не складаються з трьох елементів, генеруйте та спіймайте власний ексепшн FormulaError.

Якщо другий елемент не є «*» або «/», генеруйте та спіймайте власний ексепшн WrongOperatorError

Якщо введені числа не можуть бути float спіймайте ValueError

Також ловіть помилку при діленні на 0

В кожній спійманій помилці друкуйте пояснення, що пішло не так

Надайте три спроби скористуватись калькулятором, якщо введені не вірні дані, якщо не вийшло - прінтайте що закінчились спроби

Результат виконання формули - float число з двома знаками після крапки
"""

class FormulaError(Exception):
    pass
class WrongOperatorError(Exception):
    pass


try:
    form = input("Vvedi formulu like 2 * 5: ")
    lst = form.split()
    print(type(lst), lst)

    try:
        if len(lst) != 3:
            raise FormulaError
    except FormulaError:
        print("Nedostatochno elementov")

    x = float(lst[0])
    y = float(lst[2])
    op = lst[1]
    print(x, y, op)

    try:
        if op not in ['*','/']:
            raise WrongOperatorError
    except WrongOperatorError:
        print("Neverniy operator. Vvedite (*) ili (/)")

        if op == '*':
            res = x * y
            print(res)

    if op == '/':
        try:
            res = x / y
            print(res)
        except ZeroDivisionError as zd:
            print(f'Na NOL Delit nelzya, {zd}')

except:
    pass

