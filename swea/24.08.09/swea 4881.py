def f(i, N, curr_sum, visited):
    global min_sum

    # 모든 행에서 하나씩 숫자를 선택한 경우
    if i == N:
        # 선택된 숫자들의 합이 현재까지의 최소 합보다 작으면 갱신
        if curr_sum < min_sum:
            min_sum = curr_sum
        return

    # 현재 행에서 선택 가능한 모든 열에 대해 탐색
    for j in range(N):
        if not visited[j]:  # 아직 선택되지 않은 열이면
            visited[j] = True
            f(i + 1, N, curr_sum + arr[i][j], visited)
            visited[j] = False  # 백트래킹: 다시 되돌림

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_sum = 100*N  # 최소 합을 무한대로 초기화
    visited = [False] * N  # 각 열이 선택되었는지 여부를 추적하는 리스트
    f(0, N, 0, visited)
    print(f'#{tc} {min_sum}')