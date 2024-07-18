N = int(input())
list_1 =[]
month_date={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
for i in range(1,N+2):
    T = input()
    year =T[0:4]
    month =T[4:6]
    date =T[6:8]
    if int(month)<1 or int(month) > 12:
        print(f'#{i} -1')
    elif month_date[int(month)]<int(date):
        print(f'#{i} -1')
    else:    
        print(f'#{i} {year}/{month}/{date}')