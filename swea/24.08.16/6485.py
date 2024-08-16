T=int(input())
for tc in range(1,T+1):
    N = int(input())
    busstop = [0] * 5001
    arr= []
    for i in range(N):
        arr.append(list(map(int,input().split())))
    P =int(input())
    for i in range(N):
       for j in range(arr[i][0],arr[i][1]+1):
                busstop[j] += 1
    res=[]
    for k in range(P):
        C =int(input())
        res.append(busstop[C])

    print(f'#{tc}',*res)