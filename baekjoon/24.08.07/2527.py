for tc in range(4):
    arr=list(map(int,input().split()))
    x1=arr[0]
    y1=arr[1]
    p1=arr[2]
    q1=arr[3]
    x2=arr[4]
    y2=arr[5]
    p2=arr[6]
    q2=arr[7]
    result ='a'

    if p2 <x1 or x2 >p1 or y1 >q2 or q1 <y2:
        result ='d'
    elif x1==p2 or p1==x2:
        if q1 ==y2 or q2 ==y1:
            result ='c'
        else:
            result ='b'
    elif q1 ==y2 or q2 ==y1:
        result ='b'

    print(result)

