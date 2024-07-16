#2024-07-16
N,X=map(int,input().split())
scores =list(map(int, input().split()))
for i in range(0,N):
    if scores[i] < X:
        print(scores[i], end=" ")