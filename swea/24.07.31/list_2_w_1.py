T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr =[[0] * 10 for _ in range(10)]
    pu_num =0
    for i in range(N):
        x1,y1,x2,y2,color =map(int,input().split())
        for j in range(x1,x2+1):
            for k in range(y1,y2+1):
                if arr[j][k] != color:
                    arr[j][k] +=color
    for l in range(9):
        for a in range(9):
            if arr[l][a] ==3:
                pu_num +=1

    print(f'#{tc} {pu_num}')
