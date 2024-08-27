def order(n):
    global index
    if n==0:
        return
    else:
        order(left[n])
        arr[n]=index
        index+=1
        order(right[n])


T=int(input())
for tc in range(1,T+1):
    N = int(input())        # 1번부터 N번까지인 정점
    E = N-1
    arr = [0] * (N+1)
    left = [0]*(N+1)        # 부모를 인덱스로 왼쪽자식번호 저장
    right = [0]*(N+1)       #

    for i in range(1,N+1):
        if 2* i <=N:
            left[i] =2*i
        if 2*i+1<=N:
            right[i]=2*i+1
        if 2*i>N and 2*i+1>N:
            break
    index=1
    order(1)
    print(left)
    print(f'#{tc} {arr[1]} {arr[N//2]}')