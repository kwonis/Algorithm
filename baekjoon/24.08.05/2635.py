# N = int(input())
# max_num =0
# max_arr =[]
# for i in range(1,N+1):
#     index = 2
#     start = N
#     num = i
#     arr = [N]
#     while start - num  >=0:
#         index += 1
#         arr.append(num)
#         start_1 = num
#         num =start -num
#         start = start_1
#     if index > max_num:
#         arr.append(num)
#         max_num =index
#         max_arr =arr
#
#
# print(max_num)
# print(*max_arr)

N = int(input())
max_num = 0
max_arr = []

for i in range(1, N + 1):
    start = N
    num = i
    arr = [N, i]

    while True:
        next_num = start - num
        if next_num < 0:
            break
        arr.append(next_num)
        start = num
        num = next_num

    if len(arr) > max_num:
        max_num = len(arr)
        max_arr = arr

print(max_num)
print(*max_arr)


