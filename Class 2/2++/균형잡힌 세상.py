while True:
    s = input()
    if s == '.':
        break
    stack = []
    tmp = True
    for c in s:
        if c == '(' or c == '[':
            stack.append(c)
        elif c == ')':
            if not stack or stack[-1] == '[':
                tmp = False
                break
            elif stack[-1] == '(':
                stack.pop()
        elif c == ']':
            if not stack or stack[-1] == '(':
                tmp = False
                break
            elif stack[-1] == '[':
                stack.pop()
    print('yes' if not stack and tmp == True else 'no')