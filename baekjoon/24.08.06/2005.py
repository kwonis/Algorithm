T=int(input())
for tc in range(1,T+1):
    N=int(input())
    arr=[[0]*N for _ in range(N)]
    arr[0][0] =1
    for i in range(1,N):
        for j in range(N):
            if j == 0:
                arr[i][j]= arr[i-1][j]
            else:
                arr[i][j] = arr[i - 1][j] +arr[i-1][j-1]
    print(f'#{tc}')
    for x in range(N):
        for y in range(N):
            if arr[x][y] !=0:
                print(arr[x][y],end=' ')
        print()
