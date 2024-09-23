def is_valid(password):
    vowels = set('aeiou') # 모음 저장
    vowel_count = sum(1 for char in password if char in vowels) # 모음에 갯수
    consonant_count = len(password) - vowel_count # 자음의 갯수
    return vowel_count >= 1 and consonant_count >= 2

def back(arr, L, start, current=[]):
    if len(current) == L:
        if is_valid(current):
            print(''.join(current))
        return

    for i in range(start, len(arr)): #앞에서 부터 시작 숫서 증가 조건
        current.append(arr[i])
        back(arr, L, i + 1, current)
        current.pop()

# 입력 받기
L, C = map(int, input().split())
arr = sorted(input().split())  # 입력받은 문자들을 정렬

# 수열 생성 및 출력
back(arr, L, 0)