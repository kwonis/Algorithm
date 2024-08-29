def f(i,j,s,N,K):
    global max_v
    if max_v<s+1: # i,j 칸을 포함한 등산로 경로
        max_v =s+1
    for di,dj in [[0,1],[1,0],[0,-1],[-1,0]]:
        ni,nj =i+di,j+dj
        if 0<=ni<N and 0<=nj<N:
            if arr[i][j]>arr[ni][nj]:
                f(ni,nj,s+1,N,K)
            elif arr[i][j] > arr[ni][nj]-K:
                tap=arr[i][j]
                arr[ni][nj] =arr[i][j]-1
                f(ni,nj,s+1,N,0)
                arr[ni][nj]=tap

T=int(input())
for tc in range(1,T+1):
    N,K =map(int,input().split())
    arr=[list(map(int,input().split())) for _ in range(N)]
    start=[]
    max_h=0
    max_v=0
    for i in range(N):
        for j in range(N):
            if arr[i][j] >=max_h:
                max_h =arr[i][j]
    for i in range(N):
        for j in range(N):
            if arr[i][j] ==max_h:
                start.append((i,j))
    for i in range(len(start)):
        f(start[i][0],start[i][1],N,K)

