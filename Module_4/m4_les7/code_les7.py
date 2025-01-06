# Создайте класс TaskQueue, который будет представлять очередь задач. Этот класс должен иметь следующие методы:

# add_task(task): Добавляет задачу task в конец очереди.
# get_next_task(): Извлекает и возвращает задачу из начала очереди. Если очередь пуста, вернуть None.
# is_empty(): Проверяет, пуста ли очередь. Возвращает True, если очередь пуста, и False в противном случае.
# Создайте класс Task, который будет представлять задачу. Этот класс должен иметь атрибут:

# name: Название задачи (строка).
# Реализуйте логику работы с задачами в соответствии с их добавлением и извлечением из очереди.
class TaskQueue:
    def __init__(self):
        self.queue = []

    def add_task(self, task):
        return self.queue.append(task)
    
    def get_next_task(self):
        if len(self.queue) > 0:
            first_task = self.queue.pop(0)
            return first_task
        else:
            return None
        
    def is_empty(self):
        if not self.queue:
            return True
        else:
            return False
        
class Task:
    def __init__(self, name):
        self.name = name


queue = TaskQueue()

task1 = Task("Задача 1")
task2 = Task("Задача 2")
task3 = Task("Задача 3")

queue.add_task(task1)
queue.add_task(task2)
queue.add_task(task3)

next_task = queue.get_next_task()
print(f"Следующая задача: {next_task.name if next_task else 'Нет задач'}")  # Ожидаемый результат: "Задача 1"

queue.get_next_task()  # Извлечь следующую задачу

print(f"Очередь пуста: {queue.is_empty()}")  # Ожидаемый результат: False