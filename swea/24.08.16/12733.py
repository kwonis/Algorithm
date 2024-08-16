T = int(input())
for tc in range(1,T+1):
    N=int(input())
    arr=[list(input()) for _ in range(N)]
    di =[0,1,0,-1]
    dj =[1,0,-1,0]
    m=['A','B','C']
    h =0
    for i in range(N):
        for j in range(N):
            for k in range(4):
                ni = i
                nj = j
                if arr[i][j] in m:
                    if arr[i][j] =='A':
                        for a in range(1):
                            ni +=di[k]
                            nj += dj[k]
                        if 0<=ni<N and 0<=nj<N:
                            arr[ni][nj] ='X'
                    elif arr[i][j] =='B':
                        for b in range(2):
                            ni += di[k]
                            nj += dj[k]
                            if 0<=ni<N and 0<=nj<N:
                                arr[ni][nj] ='X'
                    elif arr[i][j] =='C':
                        for c in range(3):
                            ni += di[k]
                            nj += dj[k]
                            if 0<=ni<N and 0<=nj<N:
                                arr[ni][nj] ='X'
    for i in range(N):
        for j in range(N):
            if arr[i][j] =='H':
                h+=1
    print(f'#{tc} {h}')
