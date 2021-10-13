"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы.

Сортировка должна быть реализована в виде функции.

Обязательно доработайте алгоритм (сделайте его умнее).

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение. Обязательно сделайте замеры времени обеих реализаций
и укажите дала ли оптимизация эффективность.

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию.

Сделайте выводы!!!
Опишите в чем была ваша доработка и помогла ли вам доработка??
"""

from random import randint
from timeit import timeit
import itertools

def bubble_sort(lst):
    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1):
            if lst[j] < lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst



'''
import itertools
for i, j in itertools.product(range(len(lst) - 1), range(len(lst) - 1)):
    if j == 2 and i == 0:
        break
'''


my_lst = [randint(-100, 100) for i in range(10)]
print(my_lst)
print(f"Bubble_sort:\n{bubble_sort(my_lst[:])}")
'''
print(f"bubble_sort_improved:\n{bubble_sort_improved(my_lst[:])}")
'''
print(f"bubble_sort: {timeit('bubble_sort(my_lst[:])', globals=globals())} сек")

'''
print(f"bubble_sort_improved: {timeit('bubble_sort_improved(my_lst[:])', globals=globals())} сек")
'''