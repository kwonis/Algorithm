def fun(start,end,N,K):
    global cnt
    if start == end:
        sum =0
        length=0
        for j in range(end):
            if bit[j]:
                sum += arr[j]
                length +=1
        if length ==N and sum ==K:
            cnt+=1
    else:
        bit[start] =1
        fun(start+1,end,N,K)
        bit[start] =0
        fun(start + 1, end, N, K)

T = int(input())
for tc in range(1,T+1):
    arr =[i for i in range(1,13)]
    N,K =map(int,input().split())
    bit =[0] * 12
    cnt =0
    fun(0,12,N,K)
    print(f'#{tc} {cnt}')