def bfs(s,e,V):
    global  result
    visited =[0] * (V+1)
    q=[]
    q.append(s)
    visited[s] =1
    while q:
        t=q.pop(0)
        if t == e:
            return visited[t] -1
        for w in adjl[t]:
            if visited[w]==0:
                q.append(w)
                visited[w] = visited[t]+1

    return 0
T = int(input())
for tc in range(1,T+1):
    V,E = map(int,input().split())
    adjl =[[] for _ in range(V+1)]
    arr=[]
    result =0
    for case in range(E):
        arr.extend(list(map(int,input().split())))
    s, e = map(int, input().split())
    for i in range(E):
        v1,v2 = arr[i*2],arr[i*2+1]
        adjl[v1].append(v2)
        adjl[v2].append(v1)

    res =bfs(s,e,V)
    print(f'#{tc} {res}')

