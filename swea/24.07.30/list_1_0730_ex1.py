'''
3
5
49679
5
08271
10
7797946543
'''


T =int(input())
for tc in range(1,T+1):
    N =int(input())
    arr = list(map(int, input()))
    counts=[0] * 10
    max_num =0
    index = 0
    for i in range(0,N):
        counts[arr[i]] += 1
    for j in range(9,-1,-1):

        if counts[j] > max_num:
            max_num = counts[j]
            index =j
    print(f'#{tc} {index} {max_num}')

