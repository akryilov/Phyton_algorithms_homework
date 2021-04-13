"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы.
Сортировка должна быть реализована в
виде функции.
Обязательно доработайте алгоритм (сделайте его умнее)!
Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение.
Обязательно сделайте замеры времени обеих реализаций
и обосновать дала ли оптимизация эффективность
Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию.
Сделайте выводы!!!
Опишите в чем была ваша доработка и помогла ли вам доработка??
"""

from timeit import default_timer
from memory_profiler import memory_usage
import random


def memory_profiler(func):
    def wrap(*args, **kwargs):
        init_time = default_timer()
        init_memory = memory_usage()
        func(*args, **kwargs)
        end_time = default_timer()
        end_memory = memory_usage()
        print(f'Total time: {end_time - init_time}\n'
              f'Total memory: {end_memory[0] - init_memory[0]}')

    return wrap


@memory_profiler
def forward_sort(test_list):
    print(f'Input {test_list}')
    n = 1
    while n < len(test_list):
        for i in range(len(test_list) - n):
            if test_list[i] > test_list[i + 1]:
                test_list[i], test_list[i + 1] = test_list[i + 1], test_list[i]
        n += 1
    print(f'Output {test_list}')
    return test_list


@memory_profiler
def reverse_sort_improvement(test_list):
    print(f'Input {test_list}')
    n = 1
    while n < len(test_list):
        sort_check = 0
        for i in range(len(test_list) - n):
            if test_list[i] < test_list[i + 1]:
                test_list[i], test_list[i + 1] = test_list[i + 1], test_list[i]
                sort_check = 1
        if sort_check == 0:
            break
        n += 1
    print(f'Output {test_list}')
    return test_list


@memory_profiler
def reverse_sort(test_list):
    print(f'Input {test_list}')
    n = 1
    while n < len(test_list):
        for i in range(len(test_list) - n):
            if test_list[i] < test_list[i + 1]:
                test_list[i], test_list[i + 1] = test_list[i + 1], test_list[i]
        n += 1
    print(f'Output {test_list}')
    return test_list


list1 = list(random.randint(-100, 99) for el in range(200))
list2 = list(random.randint(-10, 9) for el in range(200))
list3 = list(random.randint(-10, 9) for el in range(200))
forward_sort(list1)
reverse_sort(list2)
reverse_sort_improvement(list3)
reverse_sort(list2)

"""
Время выполнения алгоритмов:
Прямая сортировка: 0.1018953
Обратная соритровка: 0.1027152
Обратна сортировка с проверкой совершения сортировки: 0.10269830000000002

Проверка совершения сортировки не дает премущества во времени выполнения, поскольку выполнение критерия означает,
что алгоритм уже отсортирован. 
Теоритически, проверка можеть дать преимущество только в случае использования уже отсортированного списка.
"""