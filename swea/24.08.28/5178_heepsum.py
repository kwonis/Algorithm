T=int(input())
for tc in range(1,T+1):
    N,M,L =map(int,input().split())
    arr=[list(map(int,input().split())) for _ in range(M)]
    ar =[0] *(N+1)

    for i in range(M):
        ar[arr[i][0]] = arr[i][1]

    for i in range(N,1,-1):
        ar[i//2] +=ar[i]
    print(f'#{tc} {ar[L]}')
    print(ar)
