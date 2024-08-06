bingo =[]
for b in range(5):
    bingo.extend(list(map(int,input().split())))
arr=[]
for _ in range(5):
    arr.extend(list(map(int, input().split())))
count =0

for i in arr:
    bingo[bingo.index(i)]=0
    count+=1
    big=0
    if sum(bingo[0:5]) == 0:
        big+=1
    if sum(bingo[5:10]) == 0:
        big+=1
    if sum(bingo[10:15]) == 0:
        big+=1
    if sum(bingo[15:20]) == 0:
        big+=1
    if sum(bingo[20:25]) == 0:
        big+=1
    if sum(bingo[0:25:5]) == 0:
        big+=1
    if sum(bingo[2:25:5]) == 0:
        big+=1
    if sum(bingo[3:25:5]) == 0:
        big+=1
    if sum(bingo[4:25:5]) == 0:
        big+=1
    if sum(bingo[1:25:5]) == 0:
        big+=1
    if sum(bingo[0:25:6]) == 0:
        big+=1
    if sum(bingo[4:21:4]) == 0:
        big+=1
    if big >=3:
        count
        break
print(count)