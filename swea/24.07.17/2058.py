N = int(input())

def sum_N(N):
    if N <10:
        return N
    else:
        return N%10 +sum_N(N//10)
    
print(sum_N(N))