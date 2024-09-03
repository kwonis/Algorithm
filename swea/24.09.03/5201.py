T=int(input())
for tc in range(1,T+1):
    N,M =map(int,input().split())
    box=list(map(int,input().split()))
    truck=list(map(int,input().split()))
    box.sort()
    truck.sort()
    goal=[]
    t=M-1
    b=N-1
    while t>=0 and b>=0:
        if truck[t]>=box[b]:
            goal.append(box[b])
            t-=1
            b-=1
        else:
            b-=1


    res = sum(goal)
    print(f'#{tc} {res}')
