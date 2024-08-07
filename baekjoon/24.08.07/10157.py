C,R = map(int,input().split())
K= int(input())
arr=[[0] * C for _ in range(R)]
di =[-1,0,1,0]
dj=[0,1,0,-1]
num = 1
i = R-1
j = 0
dir = 0  # 방향
res =[]
if C * R <K:
    print(0)
elif K ==1:
    print(1,1)

else:
    while num < C * R + 1:  # num가 입력 수 배열안에 들어가는 숫자까지 반복
        arr[i][j] = num  # 숫자 입력
        ni = i + di[dir]
        nj = j + dj[dir]
        if 0 <= ni < R and 0 <= nj < C and arr[ni][nj] == 0:  # 배열 넘어가거나 이미 입력되어 있는 상황 제외
            i = ni  # 기본 위치 값변경
            j = nj
        else:  # 제외 상황인 경우 방향 변경
            dir = (dir + 1) % 4
            i = i + di[dir]
            j = j + dj[dir]
        num += 1
        if num ==K:
            print(j+1,R-i)
            break