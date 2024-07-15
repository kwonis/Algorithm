#2024-07-15
list_1 =[]
for i in range(1,10):
    list_1.append(int(input()))
list_2 =sorted(list_1)
print(list_2[-1])
print(int(list_1.index(list_2[-1])+1))

