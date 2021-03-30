"""
1.	Написать программу, которая будет складывать, вычитать, умножать или делить
два числа. Числа и знак операции вводятся пользователем. После выполнения
вычисления программа не должна завершаться, а должна запрашивать новые данные
для вычислений. Завершение программы должно выполняться при вводе символа '0'
в качестве знака операции. Если пользователь вводит неверный знак
(не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и
снова запрашивать знак операции.
Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.
Подсказка:
Вариант исполнения:
- условие рекурсивного вызова - введена операция +, -, *, / - ШАГ РЕКУРСИИ
- условие завершения рекурсии - введена операция 0 - БАЗОВЫЙ СЛУЧАЙ
Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
Пример:
Введите операцию (+, -, *, / или 0 для выхода): +
Введите первое число: 214
Введите второе число: 234
Ваш результат 448
Введите операцию (+, -, *, / или 0 для выхода): -
Введите первое число: вп
Вы вместо трехзначного числа ввели строку (((. Исправьтесь
Введите операцию (+, -, *, / или 0 для выхода):
"""


def calculator():
    action = input('Enter the operation in range: +, -, *, / or 0 for exit: ')
    if action == '0':
        return 'Program closed'
    if action not in ['+', '-', '*', '/']:
        print('Please enter correct operation!')
        return calculator()
    elif action in ['+', '-', '*', '/']:
        try:
            if action in ['+', '-', '*', '/']:
                val_1 = int(input('Enter first value: '))
                val_2 = int(input('Enter second value: '))
            if action == '+':
                print('Result: {}'.format(val_1 + val_2))
            elif action == '-':
                print('Result: {}'.format(val_1 - val_2))
            elif action == '*':
                print('Result: {}'.format(val_1 * val_2))
            elif action == '/':
                try:
                    print('Result: {}'.format(val_1 / val_2))
                except ZeroDivisionError:
                    print('Zero in denominator!')
        except ValueError:
            print('Please enter correct number!')
            return calculator()
    return calculator()


calculator()
