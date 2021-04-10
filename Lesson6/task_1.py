"""
Задание 1.
Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 3-5 ваших РАЗНЫХ скриптов!
(хотя бы 3 разных для получения оценки отл).
На каждый скрипт вы должны сделать как минимум по две реализации.
Можно взять задачи с курса Основ
или с текущего курса Алгоритмов
Результаты профилирования добавьте в виде комментариев к коду.
Обязательно сделайте аналитику (что с памятью в ваших скриптах, в чем ваша оптимизация и т.д.)
ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
Попытайтесь дополнительно свой декоратор используя ф-цию memory_usage из memory_profiler
С одновременным замером времени (timeit.default_timer())!
"""

from timeit import default_timer
from memory_profiler import memory_usage
from pympler import asizeof


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
def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


@memory_profiler
def func_2(nums):
    return [i for i in range(len(nums)) if nums[i] % 2 == 0]


print('Example 1:\n')

num = list(range(1, 10000))

func_1(num)
func_2(num)

"""
Для 1000 элементов:
Total time: 0.10006739999999997
Total memory: 0.0703125
Total time: 0.09994220000000004
Total memory: 0.0

Для 10000 элементов:
Total time: 0.10151560000000004
Total memory: 0.1328125
Total time: 0.10125860000000003
Total memory: 0.0

Функция 1 использует выделение памяти под для заполнения массива.
Функции 2 достаточно первоначального выделенного объема памяти (значение Total memory = 0).
Использование функции на основе list comprehension 2 выгоднее с точки зрения расходования памяти.
"""


class FirstRoad:
    def __init__(self, length, width):
        self._length = float(length)
        self._width = float(width)
        self.__thickness = 5
        self.__weight = 25

    def mass_of_asphalt(self):
        print(f'mass of asphault is: {self._length * self._width * self.__weight * self.__thickness}')


class SecondRoad:
    __slots__ = ['_length', '_width', '__thickness', '__weight']

    def __init__(self, length, width):
        self._length = float(length)
        self._width = float(width)
        self.__thickness = 5
        self.__weight = 25

    def mass_of_asphalt(self):
        print(f'mass of asphault is: {self._length * self._width * self.__weight * self.__thickness}')


ex_1 = FirstRoad(22, 1)
ex_2 = SecondRoad(22, 1)

print('\nExample 2:\n')
print(f'Total size FirstClass: {asizeof.asizeof(ex_1)}')
print(f'Total size SecondClass: {asizeof.asizeof(ex_2)}')

"""
Total memory size FirstClass: 520
Total memory size SecondClass: 176

Результат выполнения экземпляров класса SecondClass занимает меньший объем памяти.

Использование атрибута __slots__ позволяет явно указать атрибуты экземпляров класса, что приводит
к экономии места в пямяти.
"""


@memory_profiler
def convert_to_str_cycle(int_list):
    for i in range(len(int_list)):
        int_list[i] = str(int_list[i])
    return int_list


@memory_profiler
def convert_to_str_map(int_list):
    return list(map(str, int_list))


test_list = num = list(range(0, 10000))

print('\nExample 3:\n')
convert_to_str_cycle(test_list)
convert_to_str_map(test_list)

"""
Total time: 0.10183839999999988
Total memory: 0.125
Total time: 0.10090270000000001
Total memory: 0.0703125

Реализация функции через map позволяет получить преимущество по времени выполнения и объему занимаемой памяти, 
по сравнению с реализацией функции через цикл.
"""
