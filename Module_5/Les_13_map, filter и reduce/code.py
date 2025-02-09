# 1.Используйте map(), чтобы преобразовать список чисел в список их кубов, используя обычную функцию.
def cubed(x):
    return x ** 3

numbers = [1, 2, 3, 4, 5, 6]
cube = list(map(cubed, numbers))
print('1.Cписок чисел в кубе: ', cube)

# 2.Используйте filter(), чтобы отобрать из списка чисел только те, которые делятся на 5, используя обычную функцию.
def is_even(x):
    return x % 5 == 0

numbers = [4, 5, 6, 10, 23, 3430, 2245, 43434343430, 2, 6, 7, 3, 15]
even_numbers = list(filter(is_even, numbers))
print('2.Cписок чисел, которые делятся на 5: ', even_numbers)

# 3.Используйте  filter() и  reduce(), чтобы найти произведение всех нечетных чисел в списке, используя обычную функцию.
from functools import reduce
def is_even_odd(x):
    return x % 2 != 0

def multiply(x, y):
    return x * y

numbers = [1, 2, 3, 4, 5, 6]
odd_numbers = list(filter(is_even_odd, numbers))
result = reduce(multiply, odd_numbers)
print('3.Произведение всех нечетных чисел в списке: ', result)
