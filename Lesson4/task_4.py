"""
Задание 4.
Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.
Сделайте профилировку каждого алгоритма через timeit
Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
Без аналитики задание считается не принятым
"""

import timeit
from collections import Counter
from random import randint

array = [1, 3, 1, 3, 4, 5, 1, 5, 20, 9, 1, 100, 5, 4, 2, 90, 51, 43, 6, 9, 11, 1, 0, 23, 1, 3, 5, 6, 1, 8, 923]


def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


def func_3():
    res = Counter(array).most_common()[0]
    return f'Чаще всего встречается число {res[0]}, ' \
           f'оно появилось в массиве {res[1]} раз(а)'


def func_4():
    elem = max(array, key=array.count)
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {array.count(elem)} раз(а)'


print(func_1())
print(func_2())
print(func_3())
print(func_4())

print(timeit.timeit("func_1()", number=100000, globals=globals()))  # 1.2279278
print(timeit.timeit("func_2()", number=100000, globals=globals()))  # 1.3306435
print(timeit.timeit("func_3()", number=100000, globals=globals()))  # 0.38067329999999977
print(timeit.timeit("func_4()", number=100000, globals=globals()))  # 1.1754284000000004

"""
Размер иходного массива мал, поэтому увеличил число элементов для лучшего подсчета.
Наименьшее время выполнения дает реализация алгоритма через Count.
Наибольшее время выполнения дает реализация алгоритма второй функции.
"""
