# 2024-07-15
N = int(input())
for j in range(1,N+1):
    num=list(map(int,input().split()))
    sum = 0
    n = len(num)
    for i in num:
       sum += i
    avg=sum/n
    print(avg)
    avg_1=int(round(avg,0))
    print('#'+str(j),avg_1)