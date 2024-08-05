T = int(input())
for tc in range(1, T + 1):
    in_str, word = input().split()
    w_len=len(word)
    count =0
    i=0
    while i < len(in_str):
        if in_str[i:i+(w_len)] == word:
            count +=1
            i = i+w_len
        else:
            count+=1
            i+=1

    print(f'#{tc} {count}')

