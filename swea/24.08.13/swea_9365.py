T =int(input())

for tc in range(1,T+1):
    N =int(input())
    arr =list(map(int,input().split()))
    max_i = 0
    max_cnt = 0
    for i in range(N):
        if arr[i] > max_cnt:
            max_i =i +1
            max_cnt = arr[i]
    print(f'#{tc} {max_i} {max_cnt}')