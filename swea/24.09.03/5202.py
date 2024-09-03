T= int(input())
for tc in range(1,T+1):
    N=int(input())
    arr=[list(map(int,input().split())) for _ in range(N)]
    i=1
    cnt=1
    arr.sort(key = lambda x:x[1])
    cur_h = arr[0][1]
    while i <N :
        if arr[i][0]>=cur_h:
            cur_h = arr[i][1]
            i+=1
            cnt+=1
        else:
            i+=1
    print(f'#{tc} {cnt}')

