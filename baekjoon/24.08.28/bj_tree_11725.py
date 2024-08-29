def pre_order(T):
    if T:
        res.append(T)
        pre_order(left[T])
        pre_order(right[T])


N = int(input())        # 1번부터 N번까지인 정점
E = N-1
arr = []
for i in range(N-1):
    arr.extend(list(map(int,input().split())))
left = [0]*(N+1)        # 부모를 인덱스로 왼쪽자식번호 저장
right = [0]*(N+1)       #
par = [0]*(N+1)         # 자식을 인덱스로 부모 저장
res =[]
for i in range(E):

    p, c = arr[i*2], arr[i*2+1]
    if par[c]
    if left[p]==0:          # 왼쪽자식이 없으면
        left[p] = c
    else:
        right[p] = c
    par[c] = p

c = N
while par[c]!=0:        # 부모가 있으면
    c = par[c]          # 부모를 새로운 자식으로 두고
root = c                # 더이상 부모가 없으면 root
pre_order(root)
print(res)