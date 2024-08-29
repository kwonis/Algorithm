def pre(n):
    if n == 0:
        return
    else:
        res_1.append(n)
        pre(left[n])
        pre(right[n])

def inorder(n):
    if n == 0:
        return
    else:
        inorder(left[n])
        res_2.append(n)
        inorder(right[n])

def postorder(n):
    if n == 0:
        return
    else:
        postorder(left[n])
        postorder(right[n])
        res_3.append(n)

N=int(input())
arr=[input().split() for _ in range(N)]
alpa=['.']
for i in range(N):
    alpa.append(arr[i][0])
left =[0]*(N+1)
right =[0]*(N+1)
res_1=[]
res_2=[]
res_3=[]

for i in range(N):
    p, cl,cr = alpa.index(arr[i][0]),alpa.index(arr[i][1]),alpa.index(arr[i][2])
    if left[p] == 0:  # 왼쪽자식이 없으면
        left[p] = cl
    if right[p]==0:
        right[p] = cr
pre(1)
for i in range(N):
    res_1[i] = alpa[res_1[i]]
result_1=''.join(res_1)
print(result_1)

inorder(1)
for i in range(N):
    res_2[i] = alpa[res_2[i]]
result_2=''.join(res_2)
print(result_2)

postorder(1)
for i in range(N):
    res_3[i] = alpa[res_3[i]]
result_3=''.join(res_3)
print(result_3)