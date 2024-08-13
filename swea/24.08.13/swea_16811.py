T = int(input())
for tc in range(1,T+1):
    N =int(input())
    arr=list(map(int,input().split()))
    arr.sort()
    min_num =1000
    for i in range(N-2):
        for j in range(i+1,N-1):
            if arr[i] != arr[i+1] and arr[j] !=arr[j+1]:
                s = i + 1
                m =j - i
                b =N-1-j
                if s<=N//2 and m<=N//2 and b<=N//2:
                    num =max(s,m,b) -min(s,m,b)
                    if min_num > num:
                        min_num =num
    if min_num == 1000:
        min_num =-1
    print(f'#{tc} {min_num}')


# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())  # 당근 개수
#     arr = list(map(int, input().split()))  # 당근 크기
#
#     arr.sort()  # 소, 중, 대 상자에 담기위해 크기순 정렬
#     min_v = 1000
#     for i in range(N - 2):  # 소 상자의 마지막 당근
#         for j in range(i + 1, N - 1):  # 중 상자의 마지막 당근
#             if arr[i] != arr[i + 1] and arr[j] != arr[j + 1]:  # 같은 크기 당근은 다른 상자에
#                 # 한상자에 N//2개를 초과하면 안됨. (N//2 이하로 담겨야 함)
#                 a = i + 1  # 소 상자 당근개수
#                 b = j - i  # 중 상자 당근개수
#                 c = N - 1 - j  # 대 상자 당근 개수
#                 if a <= N // 2 and b <= N // 2 and c <= N // 2:
#                     if min_v > max(a, b, c) - min(a, b, c):
#                         min_v = max(a, b, c) - min(a, b, c)
#     if min_v == 1000:  # 포장할 수 없는 경우
#         min_v = -1
#     print(f'#{tc} {min_v}')