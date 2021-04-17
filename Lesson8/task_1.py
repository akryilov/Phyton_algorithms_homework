"""
Задание 1.
Реализуйте кодирование строки "по Хаффману".
У вас два пути:
1) тема идет тяжело? тогда вы можете, опираясь на пример с урока, сделать свою!!! версию алгоритма
Разрешается и приветствуется изменение имен переменных, выбор других коллекций, различные изменения
и оптимизации.
2) тема понятна? постарайтесь сделать свою реализацию.
Вы можете реализовать задачу, например, через ООП или предложить иной подход к решению.
"""

from collections import Counter, deque


class Haffman:

    def __init__(self, test_str):
        self.test_str = test_str
        count = Counter(self.test_str)
        elems_tree = deque(sorted(count.items(), key=lambda item: item[1]))
        if len(elems_tree) != 1:
            while len(elems_tree) > 1:
                weight = elems_tree[0][1] + elems_tree[1][1]
                comb = {0: elems_tree.popleft()[0],
                        1: elems_tree.popleft()[0]}
                for i, _count in enumerate(elems_tree):
                    if weight > _count[1]:
                        continue
                    else:
                        elems_tree.insert(i, (comb, weight))
                        break
                else:
                    elems_tree.append((comb, weight))
        else:
            weight = elems_tree[0][1]
            comb = {0: elems_tree.popleft()[0], 1: None}
            elems_tree.append((comb, weight))
        self.sorted_tree = elems_tree[0][0]

    code_table = dict()

    def haffman_code(self, tree, path=''):
        if not isinstance(tree, dict):
            self.code_table[tree] = path
        else:
            self.haffman_code(tree[0], path=f'{path}0')
            self.haffman_code(tree[1], path=f'{path}1')

    def get_sorted_tree(self):
        return self.sorted_tree

    def tree_codes(self):
        self.haffman_code(self.sorted_tree)
        return self.code_table


if __name__ == '__main__':
    input_str = input("Введите строку: ")
    print(f"Трока для кодирования:\n'{input_str}'")
    haffman_str = Haffman(input_str)
    print(f'Дерево: \n{haffman_str.get_sorted_tree()}')
    print(f'Коды символов: \n{haffman_str.tree_codes()}')
    print(f'Код:')
    for i in input_str:
        print(haffman_str.tree_codes()[i], end=' ')

