#2024-07-15
A,B =map(int,input().split())

if B >=45:
    print(A,B-45)
elif B <45 and A>=1:
    print(A-1,B+60-45)
elif A ==0 and B<45:
    print(23,B+15)
    