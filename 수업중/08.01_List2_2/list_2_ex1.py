T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    max_arr=[]
    min_arr=[]
    res_arr=[0]*10
    for i in range(N - 1):  # 최소값의 인덱스에 따라 반복
        min_i = i
        for j in range(i + 1, N):  # 전체 인덱스를 비교
            if arr[min_i] > arr[j]:
                min_i = j
        arr[min_i], arr[i] = arr[i], arr[min_i]
    midle_num = N//2
    for min in range(0,N//2):
        min_arr.append(arr[min])
    for max in range(N-1,N//2-1,-1):
        max_arr.append((arr[max]))

    for fin in range(10):
        if fin % 2 ==0:
            res_arr[fin] = max_arr[fin // 2]
        else:
            res_arr[fin] = min_arr[fin // 2]
    print(f'#{tc}',*res_arr)