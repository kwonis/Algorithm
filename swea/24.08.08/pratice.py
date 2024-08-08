def dfs(s, V):
    vist =[0] * V +1
    stack =[]
    vist[s] = 1
    v = s
    for w in range(adjl[v]):
        if vist[w] == 0:
            vist[w] =1
            stack.append(w)
            v =w
            break
        else:
            if stack:
                v =stack.pop()
            else:
                break


V,E=0,0
adjl=[] # 2차배열
arr= []
for i in range(E):
    v1,v2 = arr[i*2],arr[i*2+1]
    arr[v1].append(v2)
