#재귀함수
def  a(N):
    if N ==0 or N==10:
        return 1
    else:
        return a(N-10) +a(N-20) +a(N-20)

T =int(input())
for tc in range(1,T+1):
    N =int(input())
    result = a(N)
    print(f'#{tc} {result}')

# #Meomoization
def a(N):
    global memo
    if N>=20 and memo[N]==0:
        memo[N] = a(N-10) +a(N-20) +a(N-20)
    return memo[N]

T =int(input())
for tc in range(1,T+1):
    N =int(input())
    memo = [0] * (N + 1)
    memo[0] = 1
    memo[10] = 1
    result = a(N)
    print(f'#{tc} {result}')

#DP
def a(n):
    f =[0]*(n+1)
    f[0]=1
    f[10]=1
    for i in range(20,n+1,10):
        f[i] =f[i-10]+f[i-20]+f[i-20]
    return f[n]

T=int(input())
for tc in range(1,T+1):
    N =int(input())
    result = a(N)
    print(f'#{tc} {result}')