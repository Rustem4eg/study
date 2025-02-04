# Реализация собственного класса Dict

## Описание: Представьте, что в языке Python пропали встроенные словари **(dict)**, и вам нужно создать собственный класс **MyDict**, который будет вести себя подобно словарю. Класс **MyDict** должен поддерживать следующие операции:

1. __init__(): Инициализация пустого словаря.
2. __getitem__(key): Получение значения по ключу. Если ключ не существует, вернуть None.
3. __setitem__(key, value): Установка значения по ключу.
4. __delitem__(key): Удаление элемента по ключу. Если ключ не существует, ничего не делать.
5. **keys()**: Возвращение списка всех ключей в словаре.
6. **values()**: Возвращение списка всех значений в словаре.
7. **items()**: Возвращение списка пар (ключ, значение) в словаре.
8. **__str__()**: Возврат строкового представления словаря для удобства отладки.

## Пример использования:

```
my_dict = MyDict()
my_dict['name'] = 'Alice'
my_dict['age'] = 30
print(my_dict['name'])  # Вернет 'Alice'
print('city' in my_dict)  # Вернет False
del my_dict['age']
print(my_dict.keys())  # Вернет ['name']
print(my_dict.values())  # Вернет ['Alice']
```

## Задача:

 - Напишите класс MyDict, который реализует указанные операции. Ваш класс должен обеспечивать аналогичное поведение, как у встроенных словарей в Python.