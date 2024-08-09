N =int(input())
arr = [[0] * 1001 for _ in range(1001)]
res =[]
for i in range(1,N+1):
    x,y,p,q =map(int,input().split())
    for j in range(x,x+p):
        for k in range(y,y+q):
            arr[j][k] = i
for k in range(1,N+1):
    count=0
    for i in range(1001):
        for j in range(1001):
                if arr[i][j] ==k:
                    count+=1
    res.append(count)
for i in res:
    print(i)
