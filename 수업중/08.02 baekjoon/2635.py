N = int(input())
max_num =0
max_arr =[]
for i in range(1,N):
    index = 2
    start = N
    num = i
    arr = [N]
    while start - num  >=0:
        index += 1
        arr.append(num)
        start_1 = num
        num =start -num
        start = start_1
    if index > max_num:
        arr.append(num)
        max_num =index
        max_arr =arr


print(max_num)
print(*max_arr)


