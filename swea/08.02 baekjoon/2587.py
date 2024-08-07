arr =[]
for i in range(5):
    arr.append(int(input()))
arg = sum(arr) / 5

arr.sort()

mid = arr[2]
print(int(arg))
print(mid)