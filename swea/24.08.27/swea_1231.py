def inorder(T):
    global index
    if T==0:
        return
    else:
        inorder(left[T])
        res.append(arr[T])
        inorder(right[T])


for tc in range(1,11):
    N=int(input())
    E=N-1
    left=[0] *(N+1)
    right = [0] * (N + 1)
    arr=[0] *(N+1)
    res=[]
    for i in range(N):
        a=list(input().split())
        for j in range(len(a)):
            if a[j].isdigit() ==True:
                a[j] =int(a[j])
        if len(a)== 4:
            arr[a[0]] =a[1]
            left[a[0]] =a[2]
            right[a[0]] =a[3]
        elif len(a) ==3:
            arr[a[0]] = a[1]
            left[a[0]] = a[2]
        elif len(a) ==2:
            arr[a[0]] = a[1]
    inorder(1)
    result=''.join(res)
    print(f'#{tc} {result}')
