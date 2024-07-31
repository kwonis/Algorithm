T = int(input())
for tc in range(1,T+1):
    arr=[i for i in range(1,13)]
    N,K = map(int,input().split())
    result=0
    for j in range(1 <<12):#총 12개를 가지 집합에 부분집합 수
        count = 0 #부분집합 내 요소 갯수
        sum = 0 #부분집합에 합
        for k in range(12):
            if j &(1<<k):
                sum +=arr[k] #부분집합에 합
                count +=1  #부분집합 내 요소 갯수
        if count == N and sum == K:
             result+=1 #해당 조건에 맞는 값
    print(f'#{tc} {result}')



