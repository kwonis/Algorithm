T = int(input())
for tc in range(1,T+1):
    K,N,M =map(int,input().split())
    charge=[0] * (N + 1)
    arr=list(map(int,input().split()))
    for i in range(M):
        charge[arr[i]] = 1
    current =0
    count =0
    while current +K <N:
        next =current
        for j in range(1,K+1):
            if charge[current+j] ==1:
                next =current + j

        if next ==current:
            count =0
            break
        current =next
        count +=1
    print(f'#{tc} {count}')


