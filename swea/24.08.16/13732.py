T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    a= []
    x=[]
    y=[]
    res='yes'
    for i in range(N):
        for j in range(N):
            if arr[i][j] =='#':
                a.append([i,j])
    for i in a:
        x.append(i[0])
        y.append(i[1])
    min_i =min(x)
    min_j =min(y)
    max_i =max(x)
    max_j =max(y)
    if max_i -min_i !=max_j -min_j:
        res ='no'
    for i in range(min_i,max_i+1):
        for j in range(min_j,max_j+1):
            if arr[i][j] !='#':
                res='no'
                break


    print(f'#{tc} {res}')
