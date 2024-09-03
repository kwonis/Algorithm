def check(ar, w):
    global a_jin
    global b_jin
    ar.sort()  # 정렬을 통해 연속된 숫자 체크를 용이하게 함

    # Triplet 체크
    for i in range(len(ar)):
        if ar.count(ar[i]) == 3:
            if w == 'A':
                a_jin += 1
            else:
                b_jin += 1
            return

    # Run 체크
    for i in range(len(ar) - 2):
        if ar[i] + 1 in ar and ar[i] + 2 in ar:
            if w == 'A':
                a_jin += 1
            else:
                b_jin += 1
            return


T = int(input())
for tc in range(1, T + 1):
    arr = list(map(int, input().split()))
    a = []
    b = []
    a_jin = 0
    b_jin = 0
    res = 0

    for i in range(12):
        if i % 2 == 0:
            a.append(arr[i])
            check(a, 'A')
        else:
            b.append(arr[i])
            check(b, 'B')

        # Check after every move
        if a_jin > 0:
            res = 1
            break
        elif b_jin > 0:
            res = 2
            break

    print(f'#{tc} {res}')
