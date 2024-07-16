#2024-07-15
A,B =map(int,input().split())
C =int(input())
hour = (B+C)//60
min = (B+C)%60

if A + hour <24:
    print(A+hour,min)
else:
    print(A+hour-24,min)