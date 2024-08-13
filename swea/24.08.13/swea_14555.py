T = int(input())
for tc in range(1,T+1):
    arr=list(input())
    N = len(arr)
    ball = 0
    for i in range(N):
        if arr[i] =='(':
            ball +=1
        elif arr[i] ==')' and arr[i-1] !='(':
            ball +=1

    print(f'#{tc} {ball}')
