T=int(input())
for tc in range(1,T+1):
    A = input()
    stack =[]
    result=1
    for i in A:
        if i== '(':
            stack.append(i)
        elif i==')':
            if stack:
                stack.pop()
            else:
                result=0
                break
        if i=='{':
            stack.append(i)
        elif i== '}':
            if stack:
                stack.pop()
            else:
                result=0
                break
    if stack ==[]:
        result = 1
    else:
       result =0
    print(f'#{tc} {result}')

T = int(input())
for tc in range(1, T + 1):
    A = input()
    stack = []
    result = 1

    for char in A:
        if char in '({':
            stack.append(char)
        elif char in ')}':
            if not stack:
                result = 0
                break
            top = stack.pop()
            if char == ')' and top != '(':
                result = 0
                break
            elif char == '}' and top != '{':
                result = 0
                break

    if stack:
        result = 0

    print(f'#{tc} {result}')
