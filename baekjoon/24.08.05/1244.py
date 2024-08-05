N  = int(input())
arr = list(map(int,input().split()))
P=int(input())
for peo in range(P):
    S,X =map(int,input().split())
    if S ==1:
        for i in range(X,N+1,X):
            arr[i-1] = 1 - arr[i-1]
    elif S ==2:
        if arr[X-1] == 0:
            arr[X-1] =1
        else:
            arr[X-1] =0
        for j in range(1,N//2):
            if X-j-1 <0 or X+j-1 >=N:
                break
            else:
                if arr[X-j-1] == arr[X+j-1]:
                    if arr[X-j-1]==0:
                        arr[X - j - 1]=1
                    else:
                        arr[X - j - 1] =0
                    if arr[X+j-1]==0:
                        arr[X+j-1]=1
                    else:
                        arr[X+j-1] =0
                else:
                    break

for k in range(0, N):
    print(arr[k], end=" ")
    if (k+1) % 20 == 0 :
        print()