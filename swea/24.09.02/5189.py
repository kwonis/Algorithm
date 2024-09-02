def f(x, N):
    if x == N:
        a.append(list(path))
        return
    for i in range(N):
        if i not in path:
            path.append(i)
            f(x + 1, N)
            path.pop()


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    a = []
    path = []
    path.append(0)  # 사무실(1번)에 해당하는 0번을 초기 경로에 추가
    f(1, N)  # 사무실을 방문한 상태에서 탐색 시작

    res = 100 * N  # 최대값으로 초기화
    for i in range(len(a)):
        total_cost = 0
        for j in range(N - 1):
            total_cost += arr[a[i][j]][a[i][j + 1]]
        total_cost += arr[a[i][-1]][a[i][0]]  # 마지막에서 사무실로 돌아오는 비용 추가
        if res > total_cost:
            res = total_cost
    print(a)
    print(f'#{tc} {res}')
