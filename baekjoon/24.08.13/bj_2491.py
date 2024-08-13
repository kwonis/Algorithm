N = int(input())
arr =list(map(int,input().split()))
count = 0
start = ''
max_i = 0
for i in range(N):  # 크거나 같을 때
    if start =='':
        start =i
        count +=1
        max_i = count
    elif arr[i] >=arr[i-1]:
        count +=1
        if count >max_i:
            max_i =count
    else:
        start = i
        count =1
count =0 # 카운트를 다시 초기화 시키기 (이거 때문에 틀림)
start = ''
for i in range(N): # 작거나 같을때
    if start =='':
        start =i
        count +=1
        max_i = count
    elif arr[i] <=arr[i-1]:
        count +=1
        if count >max_i:
            max_i =count
    else:
        start = i
        count =1
print(max_i)
