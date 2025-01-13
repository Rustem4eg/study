class Node:
    def __init__(self, value):
        self.value = value

        self.outbound = []
        self.inbound = []

    def point_to(self, other):
        self.outbound.append(other)
        other.inbound.append(self)

    def __str__(self):
        return f'Node({self.value})'

class Graph:
    def __init__(self, root):
        self._root = root

    def dfs(self):
        # Структуры для хранения пройденных и текущих вершин
        visited = set()  # Множество для хранения пройденных вершин
        stack = []  # Стек для хранения вершин-соседей, которые нужно пройти

        # Начальная вершина
        current = self._root

        # Основной процесс обхода
        while stack or current:
            # Проверка на завершение, если текущая вершина пуста
            if not current:
                current = stack.pop() if stack else None
                continue

            # Проверка, если вершина еще не посещена
            if current not in visited:
                visited.add(current)

                # Вывод текущей вершины
                print(f'{current}')

                # Добавление исходящих вершин в стек
                for neighbor in current.outbound:
                    stack.append(neighbor)

            # Переход к следующей вершине
            current = None
        else:
            # Если вершина уже посещена, берем следующую вершину из стека
            current = stack.pop() if stack else None

        # Добавляем начальную вершину в множество посещенных
        visited.add(self._root)

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
a.point_to(b)
b.point_to(c)
c.point_to(d)
d.point_to(a)
b.point_to(d)

g = Graph(a)

print(g.dfs())

a = Node('a')
b = Node('b')
c = Node('c')
a.point_to(b)
b.point_to(c)

g = Graph(a)
print(g.dfs())