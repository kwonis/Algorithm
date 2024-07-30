T = int(input())

for tc in range(1,T+1):
    arr=list(map(int,input()))
    counts =[0] * 12
    tri =run_1= 0
    n =0
    for i in range(0, 6):
        counts[arr[i]] += 1
    while  n <10:
        if counts[n] >=3:
            counts[n] -=3
            tri+=1
            continue
        if counts[n] >=1 and counts[n+1] >=1 and counts[n+2]>=1:
            counts[n] -=1
            counts[n-1] -= 1
            counts[n-2] -= 1
            run_1 +=1
            continue
        n+=1
    if (run_1 == 1 and tri ==1) or run_1==2 or tri ==2:
        result ='Baby Gin'
    else:
        result ='Lose'
    print(f'#{tc} {result}')
