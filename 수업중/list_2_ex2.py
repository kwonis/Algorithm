'''
3
10 3
1 2 3 4 5 6 7 8 9 10
10 5
6262 6004 1801 7660 7919 1280 525 9798 5134 1821
20 19
3266 9419 3087 9001 9321 1341 7379 6236 5795 8910 2990 2152 2249 4059 1394 6871 4911 3648 1969 2176
'''


T =int(input())

for tc in range(1,T+1):
    N,M = map(int,input().split())
    arr =list(map(int,input().split()))
    max_num = 0
    min_num = sum(arr)
    for i in range(N-M+1):
        sum_1 = 0
        for j in range(M):
            sum_1 +=arr[i+j]
        if max_num < sum_1:
            max_num =sum_1
        if min_num > sum_1:
            min_num = sum_1
    print(f'#{tc} {max_num - min_num}')