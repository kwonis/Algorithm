T =int(input())
for tc in range(1,T+1):
    N,M =map(int,input().split())
    arr=[list(map(int,input().split())) for _ in range(N)]
    max_cnt = 0
    for i in range(N):
        cnt = 0
        for j in range(M):
            if arr[i][j] ==1:
                cnt +=1
                if cnt > max_cnt and cnt >1:
                    max_cnt =cnt
            else:
                cnt=0
    for i in range(M):
        con = 0
        for j in range(N):
            if arr[j][i] ==1:
                con +=1
                if con > max_cnt and con>1:
                    max_cnt =con
            else:
                con=0
    print(f'#{tc} {max_cnt}')

