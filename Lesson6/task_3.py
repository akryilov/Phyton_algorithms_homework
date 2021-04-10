"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение!
"""
from timeit import default_timer
from memory_profiler import memory_usage


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
def counter(test_value):
    def wrap_cycle(value, even_num=0, odd_num=0):
        if value == 0:
            return 'Result: even number: {}, odd number: {}'.format(even_num, odd_num)
        else:
            operand = num % 10
            if operand % 2 == 0:
                even_num = even_num + 1
            else:
                odd_num = odd_num + 1
            wrap_cycle(value // 10, even_num, odd_num)

    return wrap_cycle(test_value)


num = int(input('Введите число:'))
counter(num)

"""
При работе с рекурсивной функцией, профилирование выполнялось бы каждый раз при вызове функции. 
Для однократного запускане обходимо обернуть рекурсивную функцию и применять декорирование к ней.
"""