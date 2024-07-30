'''
3
5
1 1 2 3 3
10
3 10 5 5 8 3 9 1 3 3
20
4 1 6 7 9 4 1 4 8 4 1 6 5 3 1 4 3 1 10 10
'''
T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    max_num = 0
    max_i =0
    min_num =float('inf')
    min_i =0
    result =0
    for i in range(N-1,-1,-1):  #최댓값에 인덱스값 구하기
        if arr[i] > max_num:
            max_num = arr[i]
            max_i = i
    for j in range(N):  #최솟값에 인덱스값 구하기
        if arr[j] < min_num:
            min_num = arr[j]
            min_i = j
    if max_i > min_i:
        result = max_i - min_i
    else:
        result = min_i-max_i
    print(f'#{tc} {result}')