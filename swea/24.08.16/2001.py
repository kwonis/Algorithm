T =int(input())
for tc in range(1,T+1):
    N,M =map(int,input().split())
    arr=[list(map(int,input().split())) for _ in range(N)]
    max_n =0
    for i in range(N-M+1):
        for j in range(N-M+1):
            sum = 0
            for k in range(i,i+M):
                for z in range(j,j+M):
                    if 0<=k<N and 0<=z<N:
                        sum +=arr[k][z]
                        if max_n < sum:
                            max_n =sum

    print(f'#{tc} {max_n}')

