N = int(input())
arr =[]
for i in range(1,N+1):
    arr.append(i)
res =[]
for j in range(N):
    if '3' in str(arr[j]) or '6' in str(arr[j]) or '9' in str(arr[j]):
        cnt =0
        for k in str(arr[j]):
            if k =='3' or k=='6' or k=='9':
                cnt+=1
        b='-'*cnt
        res.append(b)
    else:
        res.append(arr[j])
print(*res)