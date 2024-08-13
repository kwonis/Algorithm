T = int(input())

for tc in range(1,T+1):
    N,M =map(int,input().split())
    arr= list(map(int,input().split()))
    for l in range(M):
        i,j = map(int,input().split())
        for k in range(1,j+1):
            if i-k-1<0 or i-1+k>N-1:
                break
            else:
                if arr[i-1-k] == arr[i-1+k]:
                    if arr[i-1-k] ==0:
                        arr[i - 1 - k] = 1
                        arr[i - 1 + k] = 1
                    else:
                        arr[i - 1 - k] = 0
                        arr[i - 1 + k] =0

    print(f'#{tc}',*arr)

