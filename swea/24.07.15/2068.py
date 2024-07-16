# 2024-07-15
N =int(input())
for i in range(1,N+1):
    li =list(map(int,input().split()))
    li.sort()
    num = li[-1]
    print('#'+str(i),num)