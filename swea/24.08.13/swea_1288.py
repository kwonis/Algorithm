T =int(input())
for tc in range(1,T+1):
    N = int(input())
    arr=[]
    count =0
    while len(arr) !=10:
        count+=1
        num = N * count
        for i in str(num):
            arr.append(int(i))
            a = set(arr)
            arr = list(a)
    res =count *N
    print(f'#{tc} {res}')
