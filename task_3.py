"""
Задание 3.
Определить количество различных (уникальных) подстрок с использованием хеш-функции.
Дана строка S длиной N, состоящая только из строчных латинских букв.

Подсказка: примените вычисление хешей для подстрок с помощью хеш-функций и множества
Можно воспользоваться ф-цией hash() (см. материалы к уроку)

Пример:
рара - 6 уникальных подстрок

рар
ра
ар
ара
р
а
"""
import hashlib


user_set = set()
user_srt = 'papa'
for el in range(len(user_set))
    for el_a in range(el + 1, len(user_str) + 1):
        if user_srt[el:el_a] != user_srt:
            user_set.add(hashlib.cha256(user_srt[el:el_a].encode()).hexdigest())
            print(user_srt[el:el_a], end='')

print(f'\n{user_set}')
print(f'Число подстрок в выражении: {len(user_set)}')

