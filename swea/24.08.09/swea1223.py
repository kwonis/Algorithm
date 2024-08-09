for tc in range(1,11):
    N = int(input())
    infix = input()
    postfix = ''
    stack = [0] * N
    top = -1
    icp = {'+': 1, '*': 2}  # 연산자 우선순위
    for i in range(N):
        if '0' <= infix[i] <= '9':  # 피연산자인 경우
            postfix += infix[i]
        else:  # 연산자인 경우
            if top > -1 and icp[stack[top]] >= icp[infix[i]]:  # stack[top] 우선순위가 같거나 높으면  pop
                postfix += stack[top]
                top -= 1
            top += 1
            stack[top] = infix[i]
    while top > -1:     # 남아있는 연산자를 수식뒤에 붙임
        postfix += stack[top]
        top -= 1

    postfix=list(postfix)
    for i in range(N):
        if postfix[i].isdigit():
            postfix[i] = int(postfix[i])

    for i in range(N-1):
        if type(postfix[i]) == int:
            stack.append(postfix[i])
        elif postfix[i] =='*':
            x = stack.pop()
            y = stack.pop()
            res = y * x
            stack.append(res)
        elif postfix[i] =='+':
            x=stack.pop()
            y=stack.pop()
            res = y + x
            stack.append(res)
    last =stack.pop()
    last_1 =stack.pop()
    result =last + last_1
    print(f'#{tc} {result}')
