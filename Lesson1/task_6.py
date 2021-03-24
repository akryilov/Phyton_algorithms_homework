"""
Задание 6.
Задание на закрепление навыков работы с очередью
Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока
Реализуйте структуру "доска задач".
Структура должна предусматривать наличие несольких очередей задач, например
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения
После реализации структуры, проверьте ее работу на различных сценариях
"""


class QueueClass:
    def __init__(self):
        self.incoming_tasks = []  # Базовая очередь
        self.developing_tasks = []  # Очередь на доработку
        self.solved_tasks = []  # Cписок решенных задач

    def add_incoming_task(self, task):
        self.incoming_tasks.insert(0, task)

    def read_incoming_task(self):
        if len(self.incoming_tasks) > 0:
            return self.incoming_tasks[-1]
        else:
            return "No new tasks in queue"

    def get_developing_task(self):
        if len(self.developing_tasks) > 0:
            return self.developing_tasks[-1]
        else:
            return "No developing tasks in queue"

    def move_incoming_to_developing_task(self):
        self.task_to_move = self.incoming_tasks.pop()
        self.developing_tasks.insert(0, self.task_to_move)

    def move_incoming_to_solved_tasks(self):
        self.task_to_move = self.incoming_tasks.pop()
        self.solved_tasks.insert(0, self.task_to_move)

    def move_developing_to_solved_tasks(self):
        self.task_to_move = self.developing_tasks.pop()
        self.solved_tasks.insert(0, self.task_to_move)

    def tasks_lists(self):
        return self.incoming_tasks, self.developing_tasks, self.solved_tasks


new_tasks = QueueClass()
print(new_tasks.read_incoming_task())

new_tasks.add_incoming_task("1")
new_tasks.add_incoming_task("2")
new_tasks.add_incoming_task("3")

print(new_tasks.read_incoming_task())
print(new_tasks.tasks_lists())

new_tasks.move_incoming_to_developing_task()
print(new_tasks.tasks_lists())

new_tasks.move_incoming_to_solved_tasks()
print(new_tasks.tasks_lists())

new_tasks.move_developing_to_solved_tasks()
print(new_tasks.tasks_lists())
