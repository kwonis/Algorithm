def f(i,N,c,e):
    global min_c
    if i==N:
        if min_c >c:
            min_c =c
    elif c>=min_c:
        return
    else:
        f(i+1,N,c+1,battery[i]-1)

        if e>0:
            f(i+1,N,c,e-1)

T = int(input())
for tc in range(1,T+1):
    battery = list(map(int,input().split()))
    min_c =50
    f(2,battery[0],0,battery[1]-1)
    print(f'#{tc} {min_c}')