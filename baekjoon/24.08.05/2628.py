X,Y =map(int,input().split())
N =int(input())
width = [0,X]
height = [0,Y] # 높이와 길이 자르는 기준
for i in range(N):
    A ,B =map(int,input().split())
    if A ==0:
        height.append(B)
    elif A ==1:
        width.append(B)

width.sort()
height.sort()

result =0
for j in range(len(width)-1):# N,M 제외
    for k in range(len(height)-1):
        w = width[j+1] - width[j] # 자르고 난 후 결과
        h = height[k+1] - height[k]
        result = max(result,w*h)
print(result)
