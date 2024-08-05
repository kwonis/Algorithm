T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    result = ''

    # 가로에서 회문 찾기
    for i in range(N):
        for j in range(N - M + 1):
            if arr[i][j:j + M] == arr[i][j:j + M][::-1]:
                result = arr[i][j:j + M]

    # 세로에서 회문 찾기
    if not result:  # 가로에서 회문을 찾지 못한 경우
        for i in range(N):
            for j in range(N - M + 1):
                res = ''
                for k in range(M):
                    res += arr[j + k][i]
                if res == res[::-1]:
                    result = res
                    break
            if result:
                break

    print(f'#{tc} {result}')
