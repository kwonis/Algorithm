for t in range(1,11):
    tc =int(input())
    arr =list(map(int,input().split()))
    c =0
    while arr[-1] !=0:
        c+=1
        a=arr.pop(0)
        if a-c>0:
            arr.append(a-c)
        else:
            arr.append(0)
            break
        if c==5:
            c=0
    print(f'#{tc}',*arr)