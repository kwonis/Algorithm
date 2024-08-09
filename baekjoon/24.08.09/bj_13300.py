N,K =map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
man =[]
woman=[]
room=[]
count=0
for i in range(N): # 남자 여자로 나누어서 학년만 저장
    if arr[i][0] ==1:
        man.append(arr[i][1])
    else:
        woman.append(arr[i][1])
man.sort()
woman.sort()
for i in man:
    if (len(room) == 0 or i in room) and len(room) <K:# 방이 비어있거나 같은 학년이고 방에 최대 보다 작을때
        room.append(i)
        if len(room)==1: # 방에 처음 들어갈때만 방 갯수 1업
            count+=1
        if len(room) == K:
            room.clear()
    else:
        room.clear() # 학년  다를 경우 새로운방 하면서 카운트 1
        count+=1
        room.append(i)
room.clear()
for i in woman:
    if (len(room) == 0 or i in room) and len(room) <K:
        room.append(i)
        if len(room) == 1:
            count += 1
        if len(room) == K:
            room.clear()
    else:
        room.clear()
        count+=1
        room.append(i)
print(count)


