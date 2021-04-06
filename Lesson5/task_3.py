"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.
Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.
Операции равные по семантике (по смыслу)
Но разные по используемым ф-циям
И добавить аналитику, так ли это или нет.!
"""

from collections import deque
from timeit import timeit

test_deque = deque(range(1, 10000))
test_list = list(range(1, 10000))
test_list_2 = ['testlist']


def list_insert(test_list):
    test_list.insert(0, 10)
    return test_list


def deque_append(test_deque):
    test_deque.appendleft(10)
    return test_deque


print(f'list insert time:  '
      f'{timeit("list_insert(test_list)", "from __main__ import list_insert, test_list", number=10000)}')
print(f'deque append time: '
      f'{timeit("deque_append(test_deque)", "from __main__ import deque_append, test_deque", number=10000)}')


def list_pop(test_list):
    test_list.pop(0)
    return test_list


def deque_pop(test_deque):
    test_deque.popleft()
    return test_deque


print(f'list pop time:  '
      f'{timeit("list_pop(test_list)", "from __main__ import list_pop, test_list", number=10000)}')
print(f'deque pop time: '
      f'{timeit("deque_pop(test_deque)", "from __main__ import deque_pop, test_deque", number=10000)}')


def list_extend(test_list):
    test_list += test_list_2
    return test_list


def deque_extend(test_deque):
    test_deque.extendleft(test_list_2)
    return test_deque

print(f'list extend time: '
      f'{timeit("list_extend(test_list)", "from __main__ import list_extend, test_list", number=10000)}')
print(f'deque extend time: '
      f'{timeit("deque_extend(test_deque)", "from __main__ import deque_extend, test_deque", number=10000)}')

"""

Добавление и удаленине элементов просиходит значительно быстрее для deque;
Расширение списка происходит быстрее для list.

list insert time:  0.0768386
deque append time: 0.0008481000000000044
list pop time:  0.0213227
deque pop time: 0.0008483999999999992
list extend time: 0.0008061999999999792
deque extend time: 0.0010304000000000146

"""