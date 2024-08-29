def cul(n):
    if len(H[n])==1:
         return H[n][0]
    else:
        if H[n][0] =='+':
            return cul(H[n][1]) + cul(H[n][2])
        elif H[n][0] =='-':
            return cul(H[n][1]) - cul(H[n][2])
        elif H[n][0] =='*':
            return cul(H[n][1]) * cul(H[n][2])
        elif H[n][0] =='/':
            return cul(H[n][1]) // cul(H[n][2])

for tc in range(1,11):
    N =int(input())
    arr=[list(input().split()) for _ in range(N)]
    for i in range(N):
        if arr[i][1].isdigit() ==True:
            arr[i][1] =int(arr[i][1])
        else:
            arr[i][2],arr[i][3] =int(arr[i][2]),int(arr[i][3])
    H =[0] * (N+1)
    for i in range(1,N+1):
        H[i] =arr[i-1][1:] #[[0],['-',2,3],['-',4,5],[10],[88],[65]] 형식으로 저장
    print(f'#{tc} {cul(1)}')
