#  인풋 값에 전체 반복 문자 지우고 나머지 문자들로 다시 확인 하는 재귀함수


def a(arr):
    char =''
    N=len(arr)
    index =[]
    new_arr=[]
    for i in range(N):
        if i ==len(arr):
            if arr[i] == char:
                index.append(i - 1)
                index.append(i)
        else:
            if char =='':
                char = arr[i]
            elif char == arr[i]:
                index.append(i - 1)
                index.append(i)
            elif char != arr[i]:
                char =arr[i]
    set_1=set(index)
    arr_1 =list(set_1)
    if index ==[]:
        return len(arr)
    else:
        for j in range(N):
            if j not in index:
                new_arr.append(arr[j])
        return a(new_arr)


T = int(input())
for tc in range(1,T+1):
    arr =list(input())
    print(a(arr))




