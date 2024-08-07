# T =int(input())
for tc in (1,2):
    N,K =map(int,input().split(' '))
    arr = [list(map(int, input().split())) for _ in range(N)]
    count = 0
    for i in range(N):
        row =0
        cul =0
        for j in range(N):
            if arr[i][j] ==1:
                row +=1
                if row == K:
                    count+=1
            else:
                row =0

            if arr[j][i] ==1:
                cul +=1
                if cul ==K:
                    count += 1
            else:
                cul=0
    print(count)


