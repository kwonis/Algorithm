# T = int(input())
# for tc in range(1,T+1):
#     str =input()
#     string =input()
#     result = 0
#     if str in string:
#         result = 1
#     print(f'#{tc} {result}')


T = int(input())
for tc in range(1,T+1):
    str =input()
    string =input()
    str_len = 0
    string_len =0
    res =0
    for len_1 in str: #내장 함수 사용없이 길이 구하기
        str_len +=1
    for len_2 in string: #내장 함수 사용없이 길이 구하기
        string_len +=1

    for i in range(string_len - str_len +1): #string을 반복하여 슬라이싱한 곳에서 str 있는지 구하기
        if str == string[i:i+str_len]:
            res = 1
    print(f'#{tc} {res}')
