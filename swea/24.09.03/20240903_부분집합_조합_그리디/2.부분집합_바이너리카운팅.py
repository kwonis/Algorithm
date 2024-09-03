arr = ['A', 'B', 'C','D','E']
n = len(arr)


def get_sub(tar):
    cnt =0
    for i in range(n):
        if tar & 0x1:
            cnt+=1
        tar >>= 1
    return cnt
result =0
for tar in range(0, 1 << n):  # range(0, 8)
    if get_sub(tar) >=2:
        result+=1
print(result)

