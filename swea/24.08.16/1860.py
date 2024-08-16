T = int(input())
for tc in range(1,T+1):
    N,M,K =map(int,input().split())
    arr=[0] * 11112
    a= list(map(int,input().split()))
    for i in a:
        arr[i] +=1
    cur =0
    bread =0
    res ='Possible'
    max_t =max(a)
    while cur<max_t:
        if arr[0] >0:
            res='Impossible'
            break
        cur +=1
        if cur%M ==0:
            bread+=K
        if arr[cur] >0:
            if bread >= arr[cur]:
                bread -=arr[cur]
            else:
                res='Impossible'
                break
    print(f'#{tc} {res}')
