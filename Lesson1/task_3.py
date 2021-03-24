"""
Задание 3.
Для этой задачи:
1) придумайте 2-3 решения (не менее двух)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему
Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.
Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.
"""

#########

companies_info = {'HP': 1000, 'Lenovo': 1500, 'DELL': 900, 'ASUS': 2000, 'APPLE': 1800}

# Реализация первого алгоритма
# Сложность: квадратичная O(n log n)

companies_info_sorted = sorted(companies_info, key=companies_info.get, reverse=True)[:3]
print(companies_info_sorted)

# Реализация второго алгоритма
# Сложность: предполагаю, что сложность логарифмическая O(log n) и, соответственно,
# эффективность второго алгоритма выше .

companies_info_list = list(companies_info)
while len(companies_info_list) > 3:
    companies_info_list.remove(min(companies_info_list, key=companies_info.get))

print(companies_info_list)