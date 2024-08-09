def f1(i,v): # v개의 집합에서 i원소의 포함여부 결정
    if i==v: # 모든 원소에 대해 결정하면
        print(bit)
    else:
        bit[i] = 1 #a[i]가 부분 집합에 포함되는 겅우
        f1(i+1,v)
        bit[i] =0
        f1(i+1,v)

def f2(i,v,K):
    global cnt
    if i==v: # 모든 원소에 대해 결정하면
        s=0
        for j in range(v):
            if bit[j]:
                s+=a[j]
        if s==K:
            cnt +=1
    else:
        bit[i] = 1 #a[i]가 부분 집합에 포함되는 겅우
        f2(i+1,v,K)
        bit[i] =0
        f2(i+1,v,K)

def f3(i,v,N,K): # N= 부분집합의 원소수
    global cnt
    if i==v: # 모든 원소에 대해 결정하면
        s=0
        c=0
        for j in range(v):
            if bit[j]:
                s+=a[j]
                c+=1
        if c==N and s==K:
            cnt +=1
    else:
        bit[i] = 1 #a[i]가 부분 집합에 포함되는 겅우
        f3(i+1,v,N,K)
        bit[i] =0
        f3(i+1,v,N,K)
T=int(input())
for tc in range(1,T+1):
    N,K =map(int,input().split())
    a =[i for i in range(1,13)]
    bit = [0] * 12
    #재귀로 모든 부분집합 만들기
    # f1(0,12) # 총 12개의 원소,a[0]부터 포함여부 결정하기
    # ---------------
    # 부분집합의 합이 K인 경우의 수 찾기
    # ------
    # 원소의 개수가 N개이며 , 합이 K인 부분집합으 ㅣ수  cnt찾기
    cnt =0
    f3(0,12,N,K)
    print(cnt)

