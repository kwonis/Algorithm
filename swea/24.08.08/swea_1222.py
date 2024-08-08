
for tc in range(1,11):
    N= int(input())
    arr=list(input())
    for i in range(N):
        if arr[i].isdigit():
            arr[i] = int(arr[i])
    a = []
    b = []
    stack =[]
    for i in range(N):
        if type(arr[i]) != int:
            b.append(arr[i])
        else:
            a.append(arr[i])
    arr=[]
    arr.extend(a)
    arr.extend(b)
    for i in range(N-1):
        if type(arr[i]) == int:
            stack.append(arr[i])
        elif arr[i] =='+':
            x=stack.pop()
            y=stack.pop()
            res = y + x
            stack.append(res)
    last =stack.pop()
    last_1 =stack.pop()
    result =last + last_1
    print(f'#{tc} {result}')