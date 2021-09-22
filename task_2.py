"""
Задание 2.

Реализуйте два алгоритма.

Первый, в виде функции, должен обеспечивать поиск минимального значения для списка.
В основе алгоритма должно быть сравнение каждого числа со всеми другими элементами списка.
Сложность такого алгоритма: O(n^2) - квадратичная.

Второй, в виде функции, должен обеспечивать поиск минимального значения для списка.
Сложность такого алгоритма: O(n) - линейная.

Не забудьте указать сложность каждого из двух алгоритмов. Для лучшего закрепления темы
можете определить и указать сложность еще и у каждого выражения этих двух алгоритмов.

Примечание:
Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.

Постарайтесь не использовать ф-ции min() и sort() и другие ф-ции!
Подход должен быть максимально алгоритмическим.
"""

'''
    O(n^2) - квадратичная.
'''
def selection_sort(nums):

    for i in range(len(nums)):
        lowest_value_index = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[lowest_value_index]:
                lowest_value_index = j
                nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]
    random_list_of_nums = [12, 8, 3, 20, 11]
    selection_sort(random_list_of_nums)
    print(random_list_of_nums)






"""
user_list = int(567)

def name_min(user_list):
    for el in user_list:
         user_list = True
         for el_x in user_list:
             if el > el_x:
                 name_min = False
         if user_list:
             return el

print(name_min(user_list))
"""