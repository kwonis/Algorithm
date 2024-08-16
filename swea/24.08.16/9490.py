T =int(input())
for tc in range(1,T+1):
    N,M=map(int,input().split())
    arr=[list(map(int,input().split())) for _ in range(N)]
    di = [0,1,0,-1]
    dj = [1,0,-1,0]
    max_n=0
    for i in range(N):
        for j in range(M):
            sum=0
            sum += arr[i][j]
            for k in range(4):
                ni = i
                nj = j
                for l in range(arr[i][j]):
                    ni+=di[k]
                    nj+=dj[k]
                    if 0<=ni<N and 0<=nj<M:
                        sum+=arr[ni][nj]
                        if max_n < sum:
                            max_n =sum
    print(f'#{tc} {max_n}')
