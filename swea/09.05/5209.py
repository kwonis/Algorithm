def dfs(level):
    if level == len(arr):
        res.append(list(visited))
        return

    for i in range(len(arr)):
        # 가지치기 : 중복된 숫자 제거
        if arr[i] in visited:
            continue

        visited[level] = arr[i]
        dfs(level + 1)
        visited[level] = 0


T=int(input())
for tc in range(1,T+1):
    N=int(input())
    a=[list(map(int,input().split()))for _ in range(N)]
    arr=[]
    res=[]
    min_sum = 99 *N
    for j in range(1,N+1):
        arr.append(j)
    visited =[0] * N
    dfs(0)
    for i in range(len(res)):
        sum=0
        for j in range(N):
            sum +=a[j][(res[i][j])-1]
        if min_sum >sum:
            min_sum =sum
    print(f'#{tc} {min_sum}')