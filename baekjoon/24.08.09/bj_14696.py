N = int(input())

for i in range(N):
    x,*A = list(map(int,input().split()))
    y,*B = list(map(int,input().split()))
    result=''
    for i in range(4,0,-1):
        if A.count(i) > B.count(i):
             result='A'
             break
        elif A.count(i) <B.count(i):
            result ='B'
            break
        else:
            result='D'
    print(result)