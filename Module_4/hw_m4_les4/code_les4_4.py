stroka_1 = '([]{})'
stroka_2 = '([)]'
stroka_3 = '{[}'
stroka_4 = '()'

class Stack:
    def __init__(self):
        self.stroka = []

    def is_cor_br(stroka):
        while '()' in stroka or '[]' in stroka or '{}' in stroka:
            stroka = stroka.replace('()', '')
            stroka = stroka.replace('[]', '')
            stroka = stroka.replace('{}', '')
        return not stroka

print(Stack.is_cor_br(stroka_1))
print(Stack.is_cor_br(stroka_2))
print(Stack.is_cor_br(stroka_3))
print(Stack.is_cor_br(stroka_4))