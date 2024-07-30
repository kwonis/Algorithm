data =[0,4,1,3,1,2,4,1]
counts =[0] * 5 #data의 0~4까지으 ㅣ정수

N=len(data)
TEMP =[0] *N

#1단계  원소 별 개수
for x in data:
    counts[x] +=1

#2단계 누적 개수 구하기
for i in range(1,5):  #두번째부터 이전 원소의 합
    counts[i] += counts[i-1]

#3단계 : data의 맨 뒤부터 TEMP에 졍렬하기

for i in range(N-1, 0,-1):
    counts[data[i]] -=1
    TEMP[counts[data[i]]] = data[i]

print(*TEMP)

