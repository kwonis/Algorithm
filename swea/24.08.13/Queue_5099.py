# T =int(input())
# for tc in range(1,T+1):
#     N,M = map(int,input().split())
#     arr=list(map(int,input().split()))
#     fire =[]
#
#     for i in range(N):
#         fire.append(arr[i])
#     a = arr[N:]
#     res =fire[:]
#     while True:
#         for i in range(N):
#             fire[i]=fire[i]//2
#             if fire[i]==0:
#                 if len(a)>0:
#                     x =a.pop(0)
#                     fire[i] = x
#                     res[i] = x
#                 else:
#                     fire[i] =0
#                     res[i] =0
#                     if res.count(0) ==N-1:
#                         break
#         if res.count(0) == N - 1:
#             break
#     x=set(res)
#     res =list(x)
#     res.remove(0)
#     result=arr.index(res[0])+1
#     print(f'#{tc} {result}')


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    # 화덕에 넣을 피자 (번호, 치즈양)
    fire = [(i + 1, arr[i]) for i in range(N)]
    a = [(i + 1, arr[i]) for i in range(N, M)]

    while len(fire) > 1:
        # 현재 화덕에서 돌고 있는 피자를 하나 꺼내서 치즈를 반으로 줄임
        pizza_num, cheese = fire.pop(0)
        cheese //= 2

        # 치즈가 남아있다면 다시 화덕에 넣음
        if cheese > 0:
            fire.append((pizza_num, cheese))
        # 치즈가 다 녹았다면 다음 피자를 화덕에 넣음
        elif a:
            fire.append(a.pop(0))

    # 마지막 남은 피자의 번호를 출력
    print(f'#{tc} {fire[0][0]}')


