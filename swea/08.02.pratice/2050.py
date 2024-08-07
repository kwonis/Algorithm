word =list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
str = list(input())
for i in str:
    i = int(word.index(i)) +1
    print(i, end = ' ')
