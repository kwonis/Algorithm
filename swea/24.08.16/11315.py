T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    di = [0, 1, 1, 1, 0, -1, -1, -1]
    dj = [1, 1, 0, -1, -1, -1, 0, 1]
    result ='NO'
    for i in range(N):
        for j in range(N):
            if arr[i][j] =='o':
                for k in range(8):
                    x =[]
                    ni = i +di[k]
                    nj = j +dj[k]
                    while 0<=ni <N and 0<=nj <N and arr[ni][nj] =='o':
                        x.append((ni,nj))
                        ni+=di[k]
                        nj+=dj[k]
                    if len(x) ==4:
                        result ='YES'
                        break
    print(f'#{tc} {result}')