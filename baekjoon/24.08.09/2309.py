arr=[]
for i in range(9):
    arr.append(int(input()))
arr.sort()
max_sum = sum(arr)
num =max_sum - 100
lier=[]
for i in range(9):
    if len(lier) ==2: # 뺄 난쟁이 구해지면 탈출  아무거나 출력이기에 그냥 처음나오는 하나
        break
    for j in range(9):
        if arr[i] !=arr[j]:
            if arr[i]+ arr[j] ==num:
                lier.append(arr[i])
                lier.append(arr[j])
                break # 뺄 난쟁이 구해지면 탈출
result = [x for x in arr if x not in lier]
if len(result) ==7:
    for i in result:
        print(i)
