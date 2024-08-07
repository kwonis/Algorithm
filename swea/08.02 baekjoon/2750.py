T = int(input())
arr =[]
for i in range(1,T+1):# 배열에 추가해주기
    a= int(input())
    arr.append(a)

for j in range(T-1,0,-1):# 뒤집어서
    for t in range(0,j):
        if arr[t] > arr[t+1]:
            arr[t+1], arr[t] =arr[t],arr[t+1]


for k in arr:
    print(k)