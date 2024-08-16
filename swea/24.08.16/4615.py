T = int(input())
for tc in range(1,T+1):
    N,M=map(int,input().split())
    arr=[]
    di =[0,1,1,1,0,-1,-1,-1]
    dj = [1,1,0,-1,-1,-1,0,1]
    black =0
    white =0
    for i in range(M):
        arr.append(list(map(int,input().split())))
    x = [[0] * N for _ in range(N)]
    x[N//2-1][N//2-1] = 2
    x[N // 2 - 1][N // 2] = 1
    x[N // 2][N // 2 - 1] = 1
    x[N // 2][N // 2] = 2

    for i in range(M):
        x[arr[i][0] -1][arr[i][1]-1] =arr[i][2]
        for j in range(M):
            for k in range(8):
                ni = arr[i][0] -1 +di[k]
                nj = arr[i][1]-1 + dj[k]
                o =[]
                while 0<=ni<N and 0<=nj<N and x[ni][nj] !=arr[i][2] and x[ni][nj] !=0:
                    o.append((ni,nj))
                    ni +=di[k]
                    nj +=dj[k]
                if 0 <= ni < N and 0 <= nj < N and x[ni][nj] == arr[i][2]:
                    for px, py in o:
                        x[px][py] = arr[i][2]
    for i in range(N):
        for j in range(N):
            if x[i][j] ==1:
                black+1
            elif x[i][j]==2:
                white +=1

    print(f'#{tc} {black} {white}')