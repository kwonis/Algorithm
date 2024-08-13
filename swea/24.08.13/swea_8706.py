T =int(input())

for tc in range(1,T+1):
    N,M =map(int,input().split())
    arr=list(map(int,input().split()))
    length = 0
    for i in range(N):
        while arr[i]!=0:
            length +=2*(i+1)
            arr[i] = arr[i] -M
            if arr[i] < 0 and i+1<N:
                arr[i] = arr[i]+M
                arr[i+1] = arr[i+1] + arr[i]
                arr[i] =0
                length -= 2*(i+1)
            elif arr[N-1] <=0:
                break

    print(f'#{tc} {length}')
