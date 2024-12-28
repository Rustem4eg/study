# ИТОГОВОЕ ЗАДАНИЕ МОДУЛЯ 3: АННОТАЦИЯ
## ЦЕЛЬ ЗАДАНИЯ:
**Понять** и **научиться** что такое подсказки типов, как их применять к переменным, 
функциям, атрибутам и методам класса.

### Варианты аннотаций:

- Аннотации типов для переменных
- Аннотации типов для аргументов функций и возвращаемых значений
- Аннотации типов для коллекций и сложных структур данных
- Аннотации типов для пользовательских классов и объектов
- Продвинутые аннотации типов

## Документация к классам и методам, Doctest

Для чего это может понадобиться? Проекты могут быть как небольшими, состоящими из нескольких файлов, так и весьма объёмными, из сотен, или даже тысяч классов, методов, сложной логики и т.д. Как не потеряться в таком проекте? Одним из способов поддерживать проект является документирование кода. В Python для этого есть так называемые doc-string, по сути это просто строка, в которой содержится информация о классе/параметрах функции.Они описывают, что делает данный элемент кода, какие параметры он принимает, что возвращает и какие исключения может выбрасывать.

### Описание кода

- Создан класс **Engine**, который представляет двигатель автомобиля. У двигателя имеются атрибуты: 
максимальная мощность (в лошадиных силах) и тип топлива.

- Создан класс **CarBody**, который представляет кузов автомобиля. У кузова имеются атрибуты: 
тип кузова (например, седан, хэтчбек, внедорожник) и количество дверей.

- Создан класс **Wheel**, который представляет колесо автомобиля. У колеса имеются атрибуты: 
диаметр и тип резины.

- Создан класс **Car**, который представляет автомобиль. В классе Car использована композицию, 
чтобы объединить компоненты Engine, CarBody и Wheel. Каждый автомобиль должен содержать по одному 
двигателю, кузову и четыре колеса.

- Добавлены методы в класс **Car**, которые позволяют выводить информацию о каждом компоненте автомобиля, 
например, display_engine_info(), display_car_body_info(), display_wheel_info().

- Созданы несколько объектов класса **Car** с разными характеристиками (мощность двигателя, тип кузова, 
тип резины и т.д.).

- Выводится информация о каждом автомобиле с помощью методов, которые создали.