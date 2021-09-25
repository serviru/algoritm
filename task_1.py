"""
1.	Написать программу, которая будет складывать, вычитать, умножать или делить
два числа. Числа и знак операции вводятся пользователем. После выполнения
вычисления программа не должна завершаться, а должна запрашивать новые данные
для вычислений. Завершение программы должно выполняться при вводе символа '0'
в качестве знака операции. Если пользователь вводит неверный знак
(не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и
снова запрашивать знак операции.

Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.

Подсказка:
Вариант исполнения:
- условие рекурсивного вызова - введена операция +, -, *, / - ШАГ РЕКУРСИИ
- условие завершения рекурсии - введена операция 0 - БАЗОВЫЙ СЛУЧАЙ

Пример:
Введите операцию (+, -, *, / или 0 для выхода): +
Введите первое число: 214
Введите второе число: 234
Ваш результат 448
Введите операцию (+, -, *, / или 0 для выхода): -
Введите первое число: вп
Вы вместо трехзначного числа ввели строку (((. Исправьтесь
Введите операцию (+, -, *, / или 0 для выхода):

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""



def калькулятор ():

    el_3 = input('введи оператор: ')
    if el_3 == '+' and el_3 == '-' and el_3 == '*' and el_3 == '/' and el_3 == '0':
        return ('ошибка оператора')


    el_1 = int(input('введи первое 3 - х значное число: '))
    if el_1 == '0':
        return ('ввели 0')
    el_2 = int(input('введи второе 3 - х значное число: '))
    if el_2 == '0':
        return ('ввели 0')


    elif el_3 == '+':
        return el_1 + el_2
    elif el_3 == '-':
        return el_1 - el_2
    elif el_3 == '*':
        return el_1 * el_2
    elif el_3 == '/':
        return el_1 / el_2



    else:
        print('вы допустили ошибку оператора, попробуй ещё раз')
        return калькулятор ()

print(калькулятор ())
'''
OPERATIONS = { \
    "+": (lambda x, y: x + y), \
    "-": (lambda x, y: x - y), \
    "*": (lambda x, y: x * y), \
}

def calculator(expr):
    if isinstance(expr, tuple):
        return OPERATIONS[expr[1]](calculator(expr[0]), calculator(expr[2]))

    return expr

print(calculator(((1, '+', 2), '*', 3)))
'''