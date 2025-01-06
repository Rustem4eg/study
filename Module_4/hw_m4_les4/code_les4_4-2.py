stroka = input()
stack = []
is_right = True
for bracket in stroka:
    if bracket in '([{':
        stack.append(bracket)
    elif bracket in ')]}':
        if not stack:
            is_right = False
            break
        op_bracket = stack.pop()
        if op_bracket == '(' and bracket == ')':
            continue
        if op_bracket == '{' and bracket == '}':
            continue
        if op_bracket == '[' and bracket == ']':
            continue
        is_right = False
        break

if is_right and len(stack) == 0:
    print('Скобочная последовательность правильная')
else:
    print('Скобочная последовательность неправильная')