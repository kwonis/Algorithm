#levle 과 같이 거꾸로 읽어도 제대로 읽은 것과 같은 문장이나 낱말을 회문이라한다. 회문이라면 1 아니라면 0을 출력하는 프로그램을 작성하라
T =int(input())

for tc in range(1,T+1):
    str = input()
    length = len(str)
    res =1
    for i in range(length//2):
        if str[i] !=str[length-1-i]:
            res=0
            break
    print(f'#{tc} {res}')