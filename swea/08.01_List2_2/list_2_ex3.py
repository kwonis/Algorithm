T=int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    for i in range(N-1): # 최소값의 인덱스에 따라 반복
        min_i=i
        for j in range(i+1,N):# 전체 인덱스를 비교
            if arr[min_i] > arr[j]:
                min_i =j
        arr[min_i],arr[i] = arr[i],arr[min_i] # 최소값과 가장앞에 위치 변경
    print(f'#{tc}',*arr)
