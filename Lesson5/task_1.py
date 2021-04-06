"""
1.	Пользователь вводит данные о количестве предприятий, их наименования и прибыль
за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.
Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections
Пример:
Введите количество предприятий для расчета прибыли: 2
Введите название предприятия: Фирма_1
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 235 345634 55 235
Введите название предприятия: Фирма_2
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 345 34 543 34
Средняя годовая прибыль всех предприятий: 173557.5
Предприятия, с прибылью выше среднего значения: Фирма_1
Предприятия, с прибылью ниже среднего значения: Фирма_2
"""

from collections import namedtuple


def get_sum_all_comp(company_1, company_2):
    return int((company_1.first_part + company_1.second_part + company_1.third_part + company_1.fourth_part +
                company_2.first_part + company_2.second_part + company_2.third_part + company_2.fourth_part) / 4)


def get_sum_comp(company):
    return (company.first_part + company.second_part + company.third_part + company.fourth_part) / 4


def get_max_comp(company_1, company_2, sum_all_comp):
    companies_list = ""
    if sum_all_comp < get_sum_comp(company_1):
        companies_list = company_1.company_name
    if sum_all_comp < get_sum_comp(company_2):
        companies_list = companies_list + ", " + company_2.company_name
    return companies_list


def get_min_comp(company_1, company_2, sum_all_comp):
    companies_list = ""
    if sum_all_comp > get_sum_comp(company_1):
        companies_list = company_1.company_name
    if sum_all_comp > get_sum_comp(company_2):
        companies_list = companies_list + ", " + company_2.company_name
    return companies_list


Company = namedtuple('Company', 'company_name first_part second_part third_part fourth_part')

company_name_1 = input("Введите название предприятия: ")
profit_1 = list(input("Через пробел введите прибыль данного предприятия за каждый квартал(4 квартала):").split(" "))
company_1 = Company(company_name_1, int(profit_1[0]), int(profit_1[1]), int(profit_1[2]), int(profit_1[3]))

company_name_2 = input("Введите название предприятия: ")
profit_2 = list(input("Через пробел введите прибыль данного предприятия за каждый квартал(4 квартала):").split(" "))
company_2 = Company(company_name_2, int(profit_2[0]), int(profit_2[1]), int(profit_2[2]), int(profit_2[3]))

print(f"Средняя годовая прибыль всех предприятий: {get_sum_all_comp(company_1, company_2)}")
print(f"Средняя годовая прибыль первого предприятия: {get_sum_comp(company_1)}")
print(f"Средняя годовая прибыль второго предприятия: {get_sum_comp(company_2)}")
print(f"Предприятия, с прибылью выше среднего значения: "
      f"{get_max_comp(company_1, company_2, get_sum_all_comp(company_1, company_2))}")
print(f"Предприятия, с прибылью ниже среднего значения: "
      f"{get_min_comp(company_1, company_2, get_sum_all_comp(company_1, company_2))}")
