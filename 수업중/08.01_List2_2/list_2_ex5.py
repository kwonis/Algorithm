for test in range(1,11):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    di =[0,1,0,-1]
    dj =[1,0,-1,0]
    x_i = 99  # 당첨 시작되는 행 및 행에 위치
    x_j =0 #현재 열에 위치
    index =0# 도착지점
    for j in range(100): # 2가 존재하는 열값 찾기
        if arr[99][j] == 2:
            x_j =j
            break
    while x_i > 0: # 사다리 올라가기
        arr[x_i][x_j] = 0 # 지나온길 0으로 초기화
        if x_j+1 < 100 and arr[x_i][x_j+dj[0]] == 1: # 오른쪽 갈상황 인덱스를 넘지않고 1이 존재하면 오른쪽으로 이동
            nj = x_j + dj[0]
            x_j = nj #x는 움직이지 않기에 y만변동
        elif x_j-1 < 100 and arr[x_i+di[2]][x_j+dj[2]] ==1:# 왼쪽 갈상황 인덱스를 넘지않고 1이 존재하면 왼쪽으로 이동
            nj = x_j + dj[2]
            x_j = nj #x는 움직이지 않기에 y만변동
        else:
            ni = x_i + di[3]
            index = x_j
            x_i = ni  #y는 움직이지 않기에 x만 변동 및 최종에 경우 x 가 움직인 후 나오기에 y index값 저장
    print(f'#{tc} {index}')