T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [[0] * 10 for _ in range(10)]
    for test in range(N):
        x, y = map(int, input().split(' '))
        for case in range(x, y + 1):
            arr[test][case] = 1
    P = int(input())
    res_arr = {}
    for res in range(P):
        res_arr.setdefault(int(input()), 0)
    for i in range(10):
        count = 0
        for j in range(10):
            if arr[j][i] == 1:
                count += 1
                res_arr[i] = count
    res = []
    for k in list(res_arr):
        res.append(str(res_arr[k]))
    result = ' '.join(res)
    print(f'#{tc} {result}')