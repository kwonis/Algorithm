T= int(input())
for tc in range(1,T+1):
    N,K =map(int,input().split())
    arr=[list(map(int,input().split())) for _ in range(N)]
    di =[0,1]
    dj =[1,0]
    count =0
    for i in range(N):
        for j in range(N):
            if arr[i][j] ==1:
                for k in range(2):
                    res = []
                    ni = i
                    nj = j
                    while 0<=ni <N and 0<= nj<N and arr[ni][nj] ==1 and arr[ni-1][nj] != 1:
                        res.append([ni,nj])
                        ni += di[k]
                        nj += dj[k]
                    if len(res)==K:
                        count+=1
    print(count)