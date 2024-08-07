T = int(input())
for tc in range(1,T+1):
    str =input()
    string =input()
    max_count =0
    for i in str: # str에 맞는 글자 하나씩
        num = 0
        for j in string: # 긴 문자에서 하나씩 비교해서 포함 수 증가
            if i ==j:
                num +=1
            if max_count < num :
                max_count = num
    print(f'#{tc} {max_count}')