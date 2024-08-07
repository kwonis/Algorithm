T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr =list(input())
    count =0
    max_num =0
    for i in arr:
        if int(i) == 1:
            count+=1
            if count > max_num:
                max_num =count
        else:
            count = 0
    print(f'#{tc} {max_num}')