def dfs(s,V,G): # 시작점 ,정점개수, 지나가야하는 정점
    visited =[0]*(V+1) #방문 표시
    stack =[]
    visited[s] = 1
    v = s
    while True:
        for w in adjL[v]:
            if visited[w] ==0:
                stack.append(v)
                v = w
                visited[w]=1
                break
        else:
            if stack:
                v=stack.pop()
            else:
                if visited[G] ==1: # 방문정점목록에서 원하는 곳 지났는 지 확인
                    return 1
                else:
                    return 0
                break

T=int(input())
for tc in range(1,T+1):
    V,E =map(int,input().split())
    adjL = [[] for _ in range(V+1)]
    arr=[]
    for i in range(E):
        arr.extend(list(map(int,input().split())))

    for i in range(E):
        v1,v2 = arr[i*2],arr[i*2+1]
        adjL[v1].append(v2)
    S,G = map(int,input().split())
    result =dfs(S,V,G)
    print(f'#{tc} {result}')

