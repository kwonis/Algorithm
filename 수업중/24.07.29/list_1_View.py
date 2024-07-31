for tc in range(1,11):
    T = int(input())
    arr = list(map(int,input().split()))
    sum = 0
    for i in range(2,T-2):
        list_1=[]
        for j in range(-2,3):
            list_1.append(arr[i+j])
        if max(list_1) == arr[i]:
            a=arr[i]
            list_1.remove(a)
            b=max(list_1)
            sum += a-b
    print(f'#{tc} {sum}')

