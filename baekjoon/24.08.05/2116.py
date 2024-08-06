N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
dice_sum =[]
for i in range(6):
    start =i # 바닥
    result = 0 # 벽면 더한 값
    for j in range(N):
        if start ==0 or start ==5: # 연결 바닥이 둘중하나면 합이 같다.
            result+=max(arr[j][1:5]) # 벽면 중 최댓값 합
            if j != len(arr)-1 and start ==0: # 바닥이 0 일때
                start =arr[j + 1].index((arr[j][5])) # 다음 바닥을 지금의 5로
            elif j != len(arr) -1 and start ==5:
                start = arr[j + 1].index((arr[j][0]))
        elif start == 2 or start == 4:
            result += max(arr[j][0:2] + [arr[j][3]] + [arr[j][5]])
            if j != len(arr) - 1 and start == 2:
                start = arr[j + 1].index((arr[j][4]))
            elif j != len(arr) - 1 and start == 4:
                start = arr[j + 1].index((arr[j][2]))
        elif start == 1 or start == 3:
            result += max([arr[j][0]] + [arr[j][2]] + arr[j][4:])
            if j != len(arr) - 1 and start == 1:
                start = arr[j + 1].index((arr[j][3]))
            elif j != len(arr) - 1 and start == 3:
                start = arr[j + 1].index((arr[j][1]))
    dice_sum.append(result) # 각 바닥 마다에 가장 큰 벽면 합 구하고
print(max(dice_sum)) # 그중 가장 큰 값