T =int(input())
for tc in range(1,T+1):
    N= int(input())
    arr=list(input().split())
    res=[]
    if N%2 ==0:
        a=arr[:N//2]
        b=arr[N//2:]
    else:
        a=arr[:N//2+1]
        b=arr[N//2+1:]
    for i in range(N):
        if i%2==0:
            res.append(a[i//2])
        else:
            res.append(b[i//2])
    print(f'#{tc}',*res)


