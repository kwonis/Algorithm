def dfs(s,V): # 시작점 ,정점개수, 지나가야하는 정점
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
                return visited.count(1) -1
                break


V =int(input())
E = int(input())
adjL = [[] for _ in range(V+1)]
arr=[]
for i in range(E):
    arr.extend(list(map(int,input().split())))
for i in range(E):
    v1,v2=arr[i*2],arr[i*2+1]
    adjL[v1].append(v2)
    adjL[v2].append(v1)
res =dfs(1,V)
print(res)
