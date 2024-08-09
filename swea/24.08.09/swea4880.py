def f(i, j):    # i~j번까지의 승자를 찾는 함수
    if i==j:    # 한 명만 남은 경우
        return i
    else:       # 두 명 이상인 경우 두 그룹의 승자를 찾차 최종 승자를 가림
        left = f(i, (i+j)//2)       # 왼쪽 그룹의 승자
        right = f((i+j)//2+1, j)    # 오른쪽 그룹의 승자
        return win(left, right)     # 두 그룹의 승자를 찾는 함수 구현

def win (left,right):
    if arr[left] ==arr[right]:
        return left
    elif arr[left] ==1:
        if arr[right] ==3:
            return left
        elif arr[right] ==2:
            return right
    elif arr[left] ==2:
        if arr[right] ==1:
            return left
        elif arr[right] ==3:
            return right
    elif arr[left] ==3:
        if arr[right] ==2:
            return left
        elif arr[right] ==1:
            return right
T =int(input())
for tc in range(1,T+1):
    N =int(input())
    arr =[0] + list(map(int,input().split())) # 1번부터 N번 플레이어를 인덱스로 활용을 위해
    result=f(1,N)
    print(f'#{tc} {result}')