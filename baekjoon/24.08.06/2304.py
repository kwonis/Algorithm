# 전체 크기에서 해당 되지 않는 곳을 빼서 계산



N= int(input())
arr=[list(map(int,input().split())) for _ in range(N)]
arr.sort()#길이 크기 별  정렬
W=[]  #길이
H=[]  #높이
sum =0
for i in range(N):
    H.append(arr[i][1])
for j in range(N):
    W.append(arr[j][0])
Max=max(H)
Max_i=H.index((Max))
max_h =H[0] # 기본 높이 및 길이
max_w =W[0]
for i in range(Max_i+1): # 최댓값 왼쪽 먼저 계산
    if max_h < H[i]: # 가장 높은 높이보다 높아지면 계산
        h= Max-max_h #높이에 최대값에서 이전 최댓값 빼서 빼야하는 넓이 계산
        w= W[i]-max_w
        sum += h * w
        max_h =H[i] # 새로운 높이로 변경
        max_w=W[i]

max_h_r = H[-1] # 오른쪽 부분 반대로
max_w_r =W[-1]
for i in range(N-1,Max_i-1,-1):#뒤에서부터 왼쪽과 같이 작동
    if max_h_r < H[i]:
        h= Max-max_h_r
        w= W[i]-max_w_r
        sum += abs(h * w)
        max_h_r =H[i]
        max_w_r=W[i]
res = ((W[-1]-W[0]+1) * Max) -sum #전체에서 뺄 부분 빼주기
print(res)
