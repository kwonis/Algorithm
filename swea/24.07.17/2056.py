N = int(input())
list_1 =[]

for i in range(1,N+1):
    T = input()
    year =T[0:4]
    month =T[4:6]
    date = T[6:8]
    # if T[0] ==0 :
    print(f'#{i} {year}/{month}/{date}')