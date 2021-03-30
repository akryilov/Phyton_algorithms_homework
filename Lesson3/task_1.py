"""
Задание 1.
Реализуйте свои пользовательские функции, в которых реализуйте:
a) заполнение списка и словаря программно,
   сделайте замеры и сделайте выводы, что выполняется быстрее и почему
b) выполните набор операций и со списком, и со словарем,
   сделайте замеры и сделайте выводы, что и где выполняется быстрее и почему
Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)
Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор для подсчета времени работы ваших пользовательских функций
И примените ее к своим функциям!
"""
import time


def time_meas(func):
    def time_calc(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        stop_time = time.time()
        print('Meas time: {} sec'.format(stop_time - start_time))
        return res

    return time_calc


@time_meas
def create_list(list_items):
    created_list = []
    for idx in range(list_items):
        created_list.append(idx)
    return created_list


@time_meas
def create_dict(dict_items):
    created_dict = {}
    for idx in range(dict_items):
        created_dict[idx] = idx
    return created_dict


@time_meas
def item_from_list_by_idx(list, idx):
    return list[idx]


@time_meas
def item_from_list_by_value(list, item):
    for value in list:
        if value == item:
            return value


@time_meas
def item_from_dict_by_key(dict, key):
    return dict[key]


@time_meas
def item_from_dict_by_value(dict, number):
    for n in dict.values():
        if n == number:
            return n


list = create_list(100000000)  # 7.930762529373169 sec
dict = create_dict(100000000)  # 19.265626668930054 sec

"""
Добавление новых элементов в словарь происходит медленнее, т.к. при добавлении считаются хэши ключей.
"""

item_from_list_by_idx(list, 20000000)  # 0.0 sec
item_from_list_by_value(list, 20000000)  # 1.6486430168151855 sec

item_from_dict_by_key(dict, 20000000)  # 0.0 sec
item_from_dict_by_value(dict, 20000000)  # 0.661226749420166 sec
"""
Получение значений из списка по индексу происходит быстрее, чем поиск по значению.
Получение значений из словаря по ключу происходит быстрее чем по значению
Получение значений из списка и словаря по индексу (ключу) происходит за одинаковое время (?)
Получение элементов из списка и словаря по значению происходит быстрее для словаря (хотя д.б. наоборот) (?)
"""
