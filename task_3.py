"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Обязательно предложите еще свой вариант решения и также запрофилируйте!

Сделайте вывод, какая из четырех реализаций эффективнее и почему!!!

Без аналитики задание считается не принятым
"""
from cProfile import  run
from timeit import timeit

def revers_1(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


'''
n1 = input("Введите целое число: ")
n_list = list(n1)
n_list.reverse()
n2 = "".join(n_list)
print('"Обратное" ему число:', n2)

'''
'''
Сделайте вывод, какая из четырех реализаций эффективнее и почему!!!

Без аналитики задание считается не принятым

Исходя из того, что представлено на данный момент ни один из представленйх решений не
является оптимальным, исходя из замеров. Если по лаконичности, то в данной конфигурации, это 
revers_3(), срезы списка. 
'''


print(timeit("revers_1", globals=globals()))
print(timeit("revers_2", globals=globals()))
print(timeit("revers_3", globals=globals()))


