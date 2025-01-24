class MyDict:
    def __init__(self):
        self.data = []

    def __getitem__(self, key):
        for item in self.data:
            if item[0] == key:
                return item[1]
        return None

    def __setitem__(self, key, value):
        for i, item in enumerate(self.data):
            if item[0] == key:
                self.data[i] = (key, value)
                return
        self.data.append((key, value))

    def __delitem__(self, key):
        for i, item in enumerate(self.data):
            if item[0] == key:
                del self.data[i]
                return

    def keys(self):
        keys = []
        for key, _ in self.data:
            keys.append(key)
        return keys

    def values(self):
        values = []
        for _, value in self.data:
            values.append(value)
        return values

    def items(self):
        return self.data

    def __str__(self):
        return f"MyDict({self.data!r})"

# Пример использования
my_dict = MyDict()
my_dict['name'] = 'Alice'
my_dict['age'] = 30
print(my_dict['name'])  # Вернет 'Alice'
print('city' in my_dict)  # Вернет False
del my_dict['age']
print(my_dict.keys())  # Вернет ['name']
print(my_dict.values())  # Вернет ['Alice']