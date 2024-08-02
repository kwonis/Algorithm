T=int(input())
for tc in range(1,T+1):
    TC, N =input().split()
    N = int(N)
    str = list(input().split(' '))
    arr =["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    num =0
    for i in arr:
        for j in range(N):
            if i == str[j] :
                str[num] ,str[j] =str[j],str[num]
                num +=1
    print(f'#{tc}')
    print(*str)




