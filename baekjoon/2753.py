# 2024-07-15
num =int(input())
if not num % 4 ==0:
    print('0')
elif num % 100 ==0 and num % 400 != 0:
    print('0')
else:
    print('1')