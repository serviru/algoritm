"""
Задание 1.

Реализуйте свои пользовательские функции, в которых реализуйте:

a) заполнение списка и словаря,
   сделайте замеры и сделайте выводы, что выполняется быстрее и почему
   И укажите сложность каждой ф-ции, которую вы применяете для заполнения.
   У этих ф-ций может быть разная сложность. Поэтому время заполнения списка и словаря может как совпадать, так и отличаться.
b) выполните набор операций и со списком, и со словарем,
   сделайте замеры и сделайте выводы, что и где выполняется быстрее и почему
   И укажите сложность ф-ций, которые вы используете для операций.

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор для подсчета времени работы ваших пользовательских функций
И примените ее к своим функциям!

Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.
"""
'''
x = int(input('чему равен х: '))
def rec (x):

    if x >= 89:
        print(x)
        rec(x+1)




rec(2)
'''
from time import time

user_dict = {}
user_list = []
n = 10 ** 5

def cycle_decorator(watch):
    def cycle(*args, **kwargs):
        start = time()
        result = watch(*args, **kwargs)
        end = time()
        print(f'пройдено времени {watch.__name__} ' 
              f'осталось{end - start}')
        return result
    return cycle()



@cycle_decorator
def fill_list_append(lsts, nums):
    for el in range(nums):
        lsts.append(el)

fill_list_append(user_list, n)
print('_' * 100)


@cycle_decorator
def fill_list_insert(lsts, nums):
    for el in range(nums):
        lsts.insert(0, el)


fill_list_append(user_list, n)
print('_' * 100)


@cycle_decorator
def fill_dict(dcts, nums):
    for el in range(nums):
       dcts[el] = el


fill_dict(user_dict, n)
print('_' * 100)



@cycle_decorator
def change_list(lsts):
    for el in range(1000):
        lsts.pop(el)
    for el_b in range(100):
        lsts[el_b] = lsts[el_b + 1]


change_list(user_list)
print('_' * 100)



@cycle_decorator
def change_dict(dcts):
    for el in range(1000):
        dcts.pop(el)
    for el_b in range(1001, 1002):
        dcts[el_b] = 'futt'


change_dict(user_dict)
print('_' * 100)


fill_list_append(user_list, n)
print('_' * 100)


