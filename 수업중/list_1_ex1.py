'''
3
5
477162 658880 751280 927930 297191
5
565469 851600 460874 148692 111090
10
784386 279993 982220 996285 614710 992232 195265 359810 919192 158175
'''

T = int(input())
for t in range(1,T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    max =arr[0]
    for i in range(1,N):
        if max < arr[i]:
            max =arr[i]
    min = arr[0]
    for i in range(1, N):
        if min > arr[i]:
            min = arr[i]
    n = max - min
    print(f'#{t} {n}')


