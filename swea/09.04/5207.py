def binary_search(target, a):
    low = 0
    high = len(a) - 1
    cheack = ''

    while low <= high:
        mid = (low + high) // 2

        if a[mid] == target:
            return 1
        elif a[mid] > target:
            if cheack == 'l':
                break
            high = mid - 1
            cheack = 'l'
        else:
            if cheack == 'r':
                break
            low = mid + 1
            cheack = 'r'

    return 0


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    a = sorted(map(int, input().split()))
    b = list(map(int, input().split()))
    res = 0

    for i in b:
        res += binary_search(i, a)

    print(f'#{tc} {res}')
