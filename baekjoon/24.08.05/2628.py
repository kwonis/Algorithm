X,Y =map(int,input().split())
N =int(input())
arr = [[0]*X for _ in range(Y)]
for i in range(N):
    A ,B =map(int,input().split())
    if i % 2 ==0:
        print(arr[:B])

    if i % 2 ==1:
        for j in range(8):
            print(arr[j][:4])
