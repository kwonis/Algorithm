N, M = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 북, 동, 남, 서 방향 정의
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

cnt = 0  # 청소한 칸의 개수

while True:
    if arr[r][c] == 0:  # 현재 칸이 청소되지 않은 경우
        arr[r][c] = 2  # 현재 칸을 청소 (2로 표시)
        cnt += 1

    cleaned = False # 청소할 곳을 찾았는지 아닌지 확인 할 코드
    for i in range(4):
        d = (d + 3) % 4  # 반시계 방향으로 90도 회전
        ri = r + di[d]
        rj = c + dj[d]

        if 0 <= ri < N and 0 <= rj < M and arr[ri][rj] == 0:
            r, c = ri, rj  # 한 칸 전진
            cleaned = True # 청소해야할곳을 찾았다면
            break

    if not cleaned:  # 네 방향 모두 청소할 곳이 없을 때
        # 후진할 칸 계산
        ri = r - di[d]
        rj = c - dj[d]

        if 0 <= ri < N and 0 <= rj < M and arr[ri][rj] != 1:  # 벽이 아니면 후진
            r, c = ri, rj
        else:
            break  # 후진할 수 없다면 작동을 멈춤

print(cnt)
