T = int(input())
list_1 =list(input())
list_1_len=len(list_1)

for i in range(0,T-1):
    b =list(input())
    for j in range(0,list_1_len):
        if list_1[j] !=b[j]:
            list_1[j] ='?'

print(''.join(list_1))
