T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [[0] * N for _ in range(N)]
    ar = []
    for i in range(M):
        a = list(map(int,input().split()))
        ar.append(a)
    di = [0, 1, 1, 1, 0, -1, -1, -1]
    dj = [1, 1, 0, -1, -1, -1, 0, 1]
    black =0
    white=0
    # 초기 돌 배치
    arr[N // 2][N // 2] = 2
    arr[N // 2 - 1][N // 2 - 1] = 2
    arr[N // 2 - 1][N // 2] = 1
    arr[N // 2][N // 2 - 1] = 1

    # 돌 놓기
    for i in range(M):
        x = ar[i][0] - 1
        y = ar[i][1] - 1
        color = ar[i][2]
        arr[x][y] = color

        for j in range(8):  # 8방향 탐색
            nx = x + di[j]
            ny = y + dj[j]
            flip_positions = []

            while 0 <= nx < N and 0 <= ny < N and arr[nx][ny] != 0 and arr[nx][ny] != color:
                flip_positions.append((nx, ny))
                nx += di[j]
                ny += dj[j]

            # 자신의 돌을 만나면 사이의 돌들을 뒤집음
            if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == color:
                for px, py in flip_positions:
                    arr[px][py] = color

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                black += 1
            elif arr[i][j]==2:
                white += 1

    print(f'#{tc} {black} {white}')
