from dataclasses import dataclass
from enum import Enum

@dataclass
class Max_power():
    """
    Датакласс мощности двигателя
    """
    value: int
    """
    Мощность двигателя выражается в целых числах (лошадиные силы)
    """
    def __post_init__(self):
        """
        Проверка на предотвращение ввода недопустимого значения мощности двигателя,
        условие возможно изменить
        """
        if self.value < 1 or 800 < self.value:
            raise ValueError(f'Некорректное число лошадиных сил {self.value}') 

class Type_fuel(Enum):
    """
    класс для типа топлива с фиксированными видами
    """
    PETROL = 'Бензин'
    DIESEL = 'Дизель'
    ELECTRO = 'Электро'
    HYBRYD = 'Гибрид'


class Engine:
    """
    класс, представляющий двигатель автомобиля
    """
    def __init__(self, max_power: Max_power, type_fuel: Type_fuel):
        """
        создание и подготовка объектов класса Engine
        :param max_power: int: Мощность двигателя в лошадиных силах
        :param type_fuel: str: Тип топлива - выбирается из существующего класса Type_fuel
        """
        self.max_power: Max_power = max_power
        self.type_fuel: Type_fuel = type_fuel

    def __str__(self) -> str:
        """
        Вызов информации о двигателе (мощность и тип топлива)
        """
        return f'двигатель, мощностью {self.max_power.value} л.с., с типом топлива - {self.type_fuel.value}.'

@dataclass
class Door_quantity():
    value: int

    def __post_init__(self):
        if self.value < 3 or 6 < self.value:
            raise ValueError(f'Некорректное число дверей {self.value}')

class Type_body(Enum):
    SEDAN = 'Седан'
    HATCHBACK = 'Хетчбэк'
    MICROBUS = 'Микроавтобус'
    JIP = 'Джип'

class CarBody:
    def __init__(self, type_body: Type_body, doors_quantity: Door_quantity):
        self.type_body: Type_body = type_body
        self.doors_quantity: Door_quantity = doors_quantity

    def __str__(self) -> str:
        return f'кузов - "{self.type_body.value}", количество дверей {self.doors_quantity.value}'

@dataclass
class Diameter:
    value: int

    def __post_init__(self):
        if self.value < 13 or 24 < self.value:
            raise ValueError(f'Некорректный диаметр колеса {self.value}')

class Wheel_type(Enum):
    WINTER = 'Зимняя'
    SUMMER = 'Летняя'
    UNIVERS = 'Всесезонная'

class Wheel:
    def __init__(self, diameter: Diameter, wheel_type: Wheel_type):
        self.diameter: Diameter = diameter
        self.wheel_type: Wheel_type = wheel_type

    def __str__(self):
        return f'четыре колеса, диаметром {self.diameter.value} дюймов и типом "{self.wheel_type.value}"'

class Car:
    def __init__(
            self, max_power: Max_power, 
            type_fuel: Type_fuel, 
            type_body: Type_body, 
            doors_quantity: Door_quantity, 
            diameter: Diameter, 
            wheel_type: Wheel_type
            ) -> None:
        self.engine: Engine = Engine(max_power, type_fuel)
        self.carbody: CarBody = CarBody(type_body, doors_quantity)
        self.wheel: Wheel = Wheel(diameter, wheel_type)
        
    def display_engine_info(self) -> str:
        return f'Информация о двигателе: {self.engine}'
    
    def display_car_body_info(self) -> str:
        return f'Информация о кузове: {self.carbody}'
    
    def display_wheel_info(self) -> str:
        return f'Информация о колесах: {self.wheel}'
    
car_1 = Car(
    max_power=Max_power(250), 
    type_fuel=Type_fuel.PETROL, 
    type_body=Type_body.HATCHBACK,
    doors_quantity=Door_quantity(5),
    diameter=Diameter(16), 
    wheel_type=Wheel_type.SUMMER
    )
car_2 = Car(
    max_power=Max_power(500), 
    type_fuel=Type_fuel.ELECTRO, 
    type_body=Type_body.JIP,
    doors_quantity=Door_quantity(4),
    diameter=Diameter(24), 
    wheel_type=Wheel_type.UNIVERS
    )
print(car_1.display_engine_info())
print(car_1.display_car_body_info())
print(car_1.display_wheel_info())
print('====================================================================================')
print(car_2.display_engine_info())
print(car_2.display_car_body_info())
print(car_2.display_wheel_info())