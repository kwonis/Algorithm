T =int(input())
for tc in range(1,T+1):
    K,N,M =map(int,input().split())
    arr =list(map(int,input().split()))
    count =[0] * (N+1)
    count_1 =0
    for i in range(0,M):
        count[arr[i]] +=1
    for l in range(1,N,K): # K 마다 가면서 count가 1이면 한번 씩 충전
        if 1 in count[i:i+K]:
            count_1 +=1
    for j in range(0,N-1):
        if j+K+1 > N:  # 마지막 출발해서 도착지를 지나가게 되면 성공
            count_1
            break
        elif 1 not in count[j+1:j+K+1]: # 가는 사이에 주요소가 없으면 0
            count_1 =0
            break
    print(f'#{tc} {count_1}')


# T = int(input())
#
# for tc in range(1, T+1):
#     K, N, M = map(int, input().split())
#     arr = list(map(int, input().split()))
#     count = [0] * (N + 1)
#     count_1 = 0
#     # 충전기 위치를 count 리스트에 기록
#     for i in range(M):
#         count[arr[i]] += 1
#     position = 0
#     while position + K < N:
#         next_position = position
#
#         # 다음 충전 가능한 위치를 찾음
#         for i in range(1, K + 1):
#             if position + i <= N and count[position + i] == 1:
#                 next_position = position + i
#
#         # 충전할 수 없으면 종료
#         if next_position == position:
#             count_1 = 0
#             break
#
#         # 충전
#         count_1 += 1
#
#         position = next_position
#
#     print(f'#{tc} {count_1}')
