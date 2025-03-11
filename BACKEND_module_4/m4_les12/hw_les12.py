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
        visited = set()
        stack = []

        current = self._root

        while stack or current:
            if not current:
                current = stack.pop() if stack else None
                continue

            if current not in visited:
                visited.add(current)

                print(f'{current}')

                for near in current.outbound:
                    stack.append(near)

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