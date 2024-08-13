T =int(input())

for tc in range(1,T+1):
    N =int(input())
    arr =list(map(int,input().split()))
    sum_1 =0
    all = sum(arr)
    min_1=20
    min_i=0
    for i in range(N):
        sum_1 += arr[i]
        sum_2 = all -sum_1 #일꾼 2
        if abs(sum_1-sum_2) < min_1:# 최솟 값 저장 및 그때에 일꾼 1의 위치 저장장            min_1 = abs(sum_1-sum_2)
            min_i= i +1
    print(f'#{tc} {min_i} {min_1}')