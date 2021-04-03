"""
Задание 3.
Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.
Сделайте профилировку каждого алгоритма через cProfile и через timeit
Сделайте вывод, какая из трех реализаций эффективнее и почему!!!
И можете предложить еще свой вариант решения!
Без аналитики задание считается не принятым
"""

import timeit
import cProfile
from random import randint


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


num_100 = randint(10000, 1000000)
print(num_100)
print(revers_1(num_100))

cProfile.run('revers_1(num_100)')
cProfile.run('revers_2(num_100)')
cProfile.run('revers_3(num_100)')

print(timeit.timeit("revers_1(num_100)", number=1000, globals=globals()))
print(timeit.timeit("revers_2(num_100)", number=1000, globals=globals()))
print(timeit.timeit("revers_3(num_100)", number=1000, globals=globals()))

"""
Результат выполнения с использованием cProfile = 0 для каждого алгоритма.
Результат выполнения с использованием timeit показывает эффективность 3 реализации с использованием среза.
"""
