
X,Y =map(int,input().split())
N=int(input())
arr=[list(map(int,input().split())) for _ in range(N+1)]
store=[]
home=[]
end=2*X +2*Y
sum=0
for i in range(N+1): # 왼쪽 아래 꼭지점을 0으로 일자로 펼쳐서 하나의 직선으로 변경
    d =arr[i][0] # 방향
    c = arr[i][1] # 거리
    if d==1:
        w =X+X+Y-c  # 북쪽에있을때 위치 계산
    elif d==2:
        w = c # 남쪽에 있을떄
    elif d==3:
        w=X+X+Y+c #서쪽
    elif d==4:
        w = X + Y - c # 북쪽
    if i<N:
        store.append(w) #가게 상가 위치 저장
    else:
        home.append(w) # 집 위치 저장
for i in range(N):
    a=abs(store[i]-home[0]) # 절대값으로 차이
    b=end-store[i] +home[0] # 자르기 전에 가까운 경우 고려 끝에서 가게 까지 와0에서 집까지 거리
    if a >=b: # 두개 비교해서 더 짧은거 합에 더해주기
        sum+=b
    else:
        sum+=a
print(sum)

