T=int(input())
for tc in range(1,T+1):
    N =int(input())
    arr=[[0] *N for _ in range(N)]
    di =[0,1,0,-1]
    dj =[1,0,-1,0]
    num =1
    i =0
    j = 0
    dir =0 # 방향
    while num < N*N+1:  # num가 입력 수 배열안에 들어가는 숫자까지 반복
        arr[i][j] = num # 숫자 입력
        ni = i + di[dir]
        nj = j + dj[dir]
        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] ==0: # 배열 넘어가거나 이미 입력되어 있는 상황 제외
            i = ni # 기본 위치 값변경
            j = nj
        else:# 제외 상황인 경우 방향 변경
            dir = (dir+1) %4
            i = i + di[dir]
            j = j + dj[dir]
        num +=1
    print(f'#{tc}')
    for result in arr:
        print(*result)





