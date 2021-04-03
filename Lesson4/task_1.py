"""
Задание 1.
Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива
Сделайте замеры времени выполнения кода с помощью модуля timeit
Оптимизируйте, чтобы снизить время выполнения
Проведите повторные замеры
Добавьте аналитику: что вы сделали и почему!!!
Без аналитики задание считается не принятым
"""

import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


# Вариант реализации через list comprehension + enumerate
def func_2(nums):
    return [i for i, el in enumerate(nums) if el % 2 == 0]


# Вариант реализации через list comprehension + range
def func_3(nums):
    return [i for i in range(len(nums)) if nums[i] % 2 == 0]


num = list(range(1, 10000))

print(timeit.timeit("func_1(num)", number=1000, globals=globals()))  # Время выполнения 0.6661245
print(timeit.timeit("func_2(num)", number=1000, globals=globals()))  # Время выполнения 0.5853801999999999
print(timeit.timeit("func_3(num)", number=1000, globals=globals()))  # Время выполнения 0.5290005


"""Быстрее всего выполняется вариант реализации через list comprehension + range. """
