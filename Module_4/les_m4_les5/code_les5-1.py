stroka = input('Введите: ').split()
stack = []

for i in stroka:
    if i.isdigit():
        stack.append(int(i))
        continue
    elif i in '+-*/':
        if not stack:
            break
        oper_1 = stack.pop()
        oper_2 = stack.pop()
        if i == '+':
            result = int(oper_1) + int(oper_2)
        if i == '-':
            result = int(oper_1) - int(oper_2)
        if i == '*':
            result = int(oper_1) * int(oper_2)
        if i == '/':
            result = int(oper_1) / int(oper_2)
        stack.append(result)

if len(stack) == 1:
    print(stack)