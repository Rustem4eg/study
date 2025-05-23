# Урок 7: Псевдоэлементы

В этом уроке мы рассмотрим мощный инструмент CSS, известный как псевдоэлементы. Псевдоэлементы позволяют создавать и стилизовать виртуальные элементы на веб-страницах, что добавляет гибкость и креативность к дизайну.

## Что такое псевдоэлементы?

Псевдоэлементы - это виртуальные элементы, которые можно вставлять в HTML-код с помощью CSS, и они не существуют в документе в исходной разметке HTML. Они представлены двойным двоеточием :: перед именем псевдоэлемента. Наиболее часто используемые псевдоэлементы - **::before и ::after**.

### Использование псевдоэлементов

**::before:**

- Псевдоэлемент **::before** вставляет виртуальный элемент перед указанным элементом. Этот элемент можно стилизовать так же, как и обычный HTML-элемент.

<img src="/FRONTEND_module_7/5. FRONTEND_module__5/les_8/images/8-1.png" alt="Пример">


**::after:**

- Псевдоэлемент **::after** вставляет виртуальный элемент после указанного элемента. Это может быть полезно, например, для добавления дополнительного контента к ссылкам.

<img src="/FRONTEND_module_7/5. FRONTEND_module__5/les_8/images/8-2.png" alt="Пример">

### Свойство content

Свойство content является обязательным для псевдоэлементов. Оно определяет содержимое виртуального элемента. Это может быть текст, символ Unicode, URL изображения или даже атрибут элемента.

<img src="/FRONTEND_module_7/5. FRONTEND_module__5/les_8/images/8-3.png" alt="Пример">

### Преимущества использования псевдоэлементов

Псевдоэлементы могут быть полезными для создания декоративных элементов, значков и улучшения пользовательского интерфейса.
Они позволяют добавлять контент без изменения структуры HTML-кода.
Псевдоэлементы полезны для создания эффектов и декораций на элементах.

## Задание:  Найти и попробовать другие псевдоэлементы



В Мастер-классе мы с вами рассмотрели несколько примеров использования псевдоэлементов, предлагаю вам самим найти еще какие-то, попробовать и показать результат