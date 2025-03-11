class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    
    def enqueue(self, item):
       return self.queue.append(item)
    
    def dequeue(self):
        first = self.queue.pop(0)
        return first
    
    def size(self):
        return len(self.queue)
    
# Пример использования:
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print(queue.is_empty())

print("Размер очереди:", queue.size())  # Размер очереди: 3

while not queue.is_empty():
    item = queue.dequeue()
    print("Извлечен элемент:", item)

print(queue.is_empty())