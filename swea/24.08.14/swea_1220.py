# for tc in range(1,11):
#     N =int(input())
#     arr=[list(map(int,input().split())) for _ in range(N)]
#     # d=[1]
#     np =0
#     count =0
#     for i in range(N):
#         for j in range(N):
#             if np ==0:
#                 if arr[i][j] ==1:
#                     np =1
#             elif np ==1:
#                 if arr[i][j]==2:
#                     count +=1
#                     np =0
#
#     print(count)

T = 10
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0  # 교착 수
    for j in range(N):
        np = 0
        for i in range(N):
            if arr[i][j] == 2 and np == 1:
                cnt += 1
                np = 0
            elif arr[i][j] == 1:
                np = 1
    print(f'#{tc} {cnt}')
