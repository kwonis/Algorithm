T = int (input())
for tc in range(1,T+1):
    arr=list(input().split())
    stack =[]
    for i in range(len(arr)):
        if arr[i].isdigit():
            arr[i] =int(arr[i])
    for i in arr:
        if type(i) == int:
            stack.append(i)
        elif i =='.' :
            if len(stack) ==1:
                result = stack.pop()
                break
            else:
                result = 'error'
                break
        else:
            if len(stack)>=2:
                a=stack.pop()
                b=stack.pop()
                if i == '+':
                    res = b +a
                elif i =='-':
                    res = b-a
                elif i =='*':
                    res = b*a
                elif i =='/':
                    res = b//a
                stack.append(res)
            else:
                result='error'
                break
    print(f'#{tc} {result}')

