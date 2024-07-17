N = int(input())

list_1 = list(map(int,input().split()))

list_1.sort()
mid =N//2
print(list_1[mid])