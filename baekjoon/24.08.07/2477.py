K=int(input())
x =[] #가로만
y=[] # 세로만
arr=[]#전체 순서
for _ in range(6):
    a,b =map(int,input().split())
    if a >=3:
        y.append(b)
    else:
        x.append(b)
    arr.append(b)

max_x = max(x)
max_y = max(y)
max_res = max_x * max_y # 최댓값
min_res =arr[arr.index(max_x)-3]  * arr[arr.index(max_y) -3] # 빼야하는 부분을 최댓값에서 3번째전에 나오는 숫자로 알고 계산

res=max_res -min_res
result =res * K

print(result)
