def f(i,j,s):
    global min_n
    if i>=N or j >=N:
        return
    elif i==N-1 and j == N-1:
        s+=arr[i][j]
        if min_n >s:
            min_n =s
    else:
        f(i+1,j,s+arr[i][j])
        f(i,j+1,s+arr[i][j])

T=int(input())
for tc in range(1,T+1):
    N=int(input())
    arr= [list(map(int,input().split())) for _ in range(N)]
    a=[]
    min_n =10 *N*N
    f(0,0,0)
    print(min_n)



# def f(i, j, s):
#     global min_n
#     if i >= N or j >= N:  # 배열 범위를 벗어나는 경우
#         return
#     elif i == N-1 and j == N-1:  # 오른쪽 아래 끝에 도달한 경우
#         s += arr[i][j]
#         if min_n > s:
#             min_n = s
#     else:
#         f(i + 1, j, s + arr[i][j])  # 아래로 이동
#         f(i, j + 1, s + arr[i][j])  # 오른쪽으로 이동
#
# T = int(input())  # 테스트 케이스 수 입력
# for tc in range(1, T + 1):
#     N = int(input())  # N 입력
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     min_n = 10 * N * N  # 최솟값 초기화
#     f(0, 0, 0)  # 재귀 호출
#     print(f"#{tc} {min_n}")  # 결과 출력
