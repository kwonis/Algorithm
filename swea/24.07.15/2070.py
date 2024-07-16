# 2024-07-15
N = int(input())
for i in range(1,N+1):
    A,B =map(int,input().split())
    result =0
    if A > B:
        result = '>'
    elif A==B:
        result ='='
    else:
        result = '<'

        
    print('#'+str(i),result)