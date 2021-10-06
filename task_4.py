"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""


from collections import OrderedDict
from timeit import timeit


def dict_builder(user_dict):
    user_dict = {el: el ** el for el in range(500)}
    return user_dict


def dict_search(user_dict):
    return user_dict.get(499)


def dict_pop(user_dict):
    user_dict = {el: el ** el for el in range(500)}
    for i in range(25):
        user_dict.pop(i)
    return user_dict


dct = {}
ord_dct = OrderedDict()
dct = dict_builder(dct)
ord_dct = dict_builder(ord_dct)

print(timeit('dict_builder(dct)', globals=globals(), number=1000))
print(timeit('dict_builder(ord_dct)', globals=globals(), number=1000))

print(timeit('dict_search(dct)', globals=globals(), number=100000))
print(timeit('dict_search(ord_dct)', globals=globals(), number=100000))

print(timeit('dict_pop(dct)', globals=globals(), number=1000))
print(timeit('dict_pop(ord_dct)', globals=globals(), number=1000))

'''
Исходя из выполненых замеров словорей и финкция OrderedDict не имеет преимущество, а значит не имеет смысла её применение
в настоящее время

'''