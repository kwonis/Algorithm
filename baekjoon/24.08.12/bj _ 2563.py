N = int(input())
arr = [[0] *100 for _ in range(100)]
a = [list(map(int,input().split())) for i in range(N)]
count =0
for i in range(N):
    for j in range(a[i][0],a[i][0]+10):
        for k in range(a[i][1],a[i][1]+10):
            if arr[j][k] != 1:
                arr[j][k] = 1
                count +=1
print(count)