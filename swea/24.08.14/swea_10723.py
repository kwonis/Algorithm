def fstart(N):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return i, j
    return -1, -1

def bfs(i, j, N):      # 재귀
    visited = [[0] * N for _ in range(N)]
    q=[]
    q.append([i,j])
    visited[i][j] = 1
    di =[0,1,0,-1]
    dj =[1,0,-1,0]
    while q:
        ni,nj =q.pop(0)
        if maze[ni][nj] ==3:
            return  visited[ni][nj] -2
        for k in range(4):
            if 0 <= ni + di[k] < N and 0 <= nj + dj[k] < N and maze[ni + di[k]][nj + dj[k]] != 1 and visited[ni + di[k]][nj + dj[k]] == 0:
                q.append([ni + di[k], nj + dj[k]])
                visited[ni + di[k]][nj + dj[k]] = visited[ni][nj] + 1
    return 0



T =int(input())
for tc in range(1,T+1):
    N = int(input())
    maze =[list(map(int,input())) for _ in range(N)]
    sti,stj =fstart(N)
    print(f'#{tc} {bfs(sti, stj, N)}')
