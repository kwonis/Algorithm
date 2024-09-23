def back(arr, M, s=[]):
    if len(s) == M:
        print(' '.join(map(str, s)))
        return

    for num in sorted(set(arr)):  # 중복 제거 및 정렬
        s.append(num)
        back(arr, M, s)
        s.pop()


# 입력 받기
N, M = map(int, input().split())
arr = list(map(int, input().split()))

# 수열 생성 및 출력
back(arr, M)