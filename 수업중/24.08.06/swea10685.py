T = int(input())
for tc in range(1,T+1):
    arr =list(input())
    N=len(arr)
    stack =[]
    i= -1
    while i <N-1:
        i+=1
        if stack == []:
            stack.append(arr[i])
        else:
            K = stack.pop()
            if K == arr[i]:
                arr.pop(i - 1)
                arr.pop(i - 1)
                i = -1
                stack=[]
                N=len(arr)
            else:
                stack.append(K)
                stack.append(arr[i])

    print(f'#{tc} {len(arr)}')

