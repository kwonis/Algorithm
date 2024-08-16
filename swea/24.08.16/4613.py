T = int(input())
for tc in range(1,T+1):
    N,M =map(int,input().split())
    arr =[list(input()) for _ in range(N)]
    count = 0
    min_c =3000
    W = [0] * N
    B = [0] * N
    R = [0] * N
    for i in range(N):
        for j in range(M):
            if arr[i][j] !='W':
                W[i] +=1
            if arr[i][j]!='B':
                B[i]+=1
            if arr[i][j] !='R':
                R[i]+=1
    for w in range(0,N-2):
        for b in range(w+1,N-1):
            sum_1 = 0
            sum_1+=sum(W[:w+1]) +sum(B[w+1:b+1]) +sum(R[b+1:])
            if sum_1 <min_c:
                min_c = sum_1

    print(f'#{tc} {min_c}')