def pre_order(T):
    global count
    if T:
        count+=1
        pre_order(left[T])
        pre_order(right[T])


T= int(input())
for tc in range(1,T+1):
    E,N =map(int,input().split())
    arr = list(map(int, input().split()))
    left =[0] *(E+2)
    right=[0]*(E+2)
    par=[0] *(E+2)
    count =0
    for i in range(E):
        p,c =arr[i*2],arr[i*2+1]

        if left[p]==0:
            left[p] =c
        else:
            right[p]=c
        par[c]=p
    pre_order(N)
    print(f'#{tc} {count}')