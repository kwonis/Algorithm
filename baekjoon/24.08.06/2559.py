import sys
N,K=map(int,sys.stdin.readline().split())
arr=list(map(int,input().split()))
sum_1 =sum(arr[:K])
max_sum =sum_1
for i in range(N-K):
    sum_1 += arr[i+K] -arr[i] #앞에 더해주고 하나 빼주고
    if max_sum < sum_1:
        max_sum =sum_1


print(max_sum)
