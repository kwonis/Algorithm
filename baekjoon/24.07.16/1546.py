#2024-07-16
n=int(input())
scores =list(map(int, input().split()))
max=max(scores)
sum =sum(scores)

print(sum * 100 / max / n)