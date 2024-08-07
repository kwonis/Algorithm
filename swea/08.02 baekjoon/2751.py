T = int(input())
arr =[]
for i in range(1,T+1):# 배열에 추가해주기
    a= int(input())
    arr.append(a)
arr.sort()
for k in arr:
    print(k)