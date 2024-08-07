for tc in range(1,11):
    D =int(input())
    arr =list(map(int,input().split()))  #길이 0~99 100개
    dump =0
    result =2
    while dump <= D:
        max_num = 0
        min_num = 100
        max_i = 0
        min_i = 0
        for i in range(0,100):
            if max_num < arr[i]:
                max_num = arr[i]
                max_i =i
        for j in range(0,100):
            if min_num > arr[j]:
                min_num =arr[j]
                min_i =j
        arr[max_i] -= 1
        arr[min_i] += 1
        if max_num - min_num <=1:
            result = max_num - min_num
            break
        else:
            result =max_num-min_num
        dump+=1
    print(f'#{tc} {result}')

