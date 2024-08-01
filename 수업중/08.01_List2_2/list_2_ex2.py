T = int(input())
for tc in range(1,T+1):
    P,Pa,Pb =map(int,input().split())
    mid_a=0
    mid_b=0
    ra=P
    rb=P
    count_a = 0
    count_b = 0
    l_a = 1
    l_b= 1
    result =''
    while count_a<P:
        mid_a = (l_a + ra)//2
        if Pa > mid_a:
            l_a = mid_a
            count_a +=1
        elif Pa < mid_a:
            ra =mid_a
            count_a += 1
        else:
            count_a += 1
            break
    while count_b <P:
        mid_b = (l_b + rb) // 2
        if Pb > mid_b:
            l_b = mid_b
            count_b += 1
        elif Pb < mid_b:
            rb = mid_b
            count_b += 1
        else:
            count_b += 1
            break
    if count_a < count_b:
        result ='A'
    elif count_a > count_b:
        result = 'B'
    else:
        result =0
    print(f'#{tc} {result}')