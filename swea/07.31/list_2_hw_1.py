T = int(input())
for tc in range(1,T+1):
    N,M =map(int,input().split())
    arr =[list(map(int,input().split())) for _ in range(N)]
    max_n =0
    for i in range(N):
        for j in range(N):#파리가 있는 표
            sum =0
            for k in range(M): # 파리채모양 표
                for a in range(M):
                    if i+k <N and j+a <N: # 파리채가 전체판을 넘어갈경우를 막기
                        sum +=arr[i+k][j+a]
                        if max_n <sum:
                            max_n = sum
    print(f'#{tc} {max_n}')

