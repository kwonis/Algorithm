T = int(input())
for tc in range(1,T+1):
    N,M =map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    k = abs(N-M)
    max_sum =0
    if N <=M:
        for i in range(k+1):
            sum =0
            for j in range(N):
                sum +=a[j] *b[j+i]
            if sum > max_sum:
                max_sum =sum
    else:
        for i in range(k):
            sum =0
            for j in range(M):
                sum +=b[j] *a[j+i]
            if sum > max_sum:
                max_sum =sum
    print(f'#{tc} {max_sum}')