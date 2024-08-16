T=int(input())
for tc in range(1,T+1):
    N,Q=map(int,input().split())
    a=[0] * N
    arr=[]
    for i in range(Q):
        arr.append(list(map(int,input().split())))

    for i in range(Q):
        L,R =arr[i]
        for j in range(L-1,R):
            a[j] =i+1
    print(f'#{tc}',*a)
