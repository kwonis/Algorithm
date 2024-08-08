def dfs(i, j, N, arr):
    stack = [(i, j)] # 움직인 곳을 스택에 저장
    visited = [[False] * N for _ in range(N)] # 전체 미로 생성
    visited[i][j] = True # 지나간 곳 변경

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    while stack:
        i, j = stack.pop() # 시작점

        for dir in range(4): # 방향 변경
            ni = i + di[dir]
            nj = j + dj[dir]

            if 0 <= ni < N and 0 <= nj < N: # 배열안에서만 작동하게
                if arr[ni][nj] == 3: # 도착점이면 1리턴
                    return 1
                if arr[ni][nj] == 0 and not visited[ni][nj]: # 미로에서 갈수 있는 곳이 간적 없으면
                    visited[ni][nj] = True # 지나간 곳 체크
                    stack.append((ni, nj)) # 지나갔으므로 스택 저장

    return 0 # 더이상 갈 곳 및 돌아갈곳이 없으면 0 리턴


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().strip())) for _ in range(N)]
    si, sj = -1, -1
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                si, sj = i, j
                break
        if si != -1:
            break

    result = dfs(si, sj, N, arr)

    print(f'#{tc} {result}')
