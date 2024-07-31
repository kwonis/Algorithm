T = int(input())
for tc in range(1,T+1):
    N,M =map(int,input().split())
    arr =[list(map(int,input().split())) for _ in range(N)]
    di = [0,0, 1, 0, -1]
    dj = [0,1, 0, -1, 0]
    max_num = 0
    for i in range(N):
        for j in range(M):
            s = 0
            for k in range(5):
                ni =i +di[k]
                nj =j +dj[k]
                if 0<=ni<N and 0<=nj <M:
                    s += arr[ni][nj]
            if max_num < s:
                max_num =s
    print(f'#{tc} {max_num}')