T = int(input())
for tc in range(1,T+1):
    arr=list(input())
    N=len(arr)
    a =[0] * N
    for i in range(N):
        if arr[i] =='(':
            if arr[i+1] ==')':
                 