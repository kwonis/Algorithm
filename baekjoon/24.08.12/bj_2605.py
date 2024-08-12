N=int(input())
res =[]
X = list(map(int,input().split()))
result=[]
for i in range(N): # 전체 인원
    res.append(i+1)

for j in range(N):
    for k in range(j+1):
        if X[j] ==k: # 뽑은 값 확인
            a=res[k]
            result.insert(j-k,j+1)

print(*result)



