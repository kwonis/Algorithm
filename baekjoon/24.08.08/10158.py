# X,Y = map(int,input().split())
# arr=[[0] * (X+1) for i in range(Y+1)]
# sx,sy =map(int,input().split())
# T=int(input())
# sy = Y-sy
# di = [-1 ,-1,1,-1]
# dj = [1,-1,-1,-1]
# dir =0
# for i in range(T):
#     ni =sy + di[dir]
#     nj = sx +dj[dir]
#     if 0<= ni <=Y and 0<=nj<=nj:
#         sy = ni
#         sx = nj
#         if ni==Y or nj == X or ni ==0 or nj ==0:
#             dir = (dir + 1) % 4
#     else:
#         dir =(dir+1) % 4
#         sy = sy +di[dir]
#         sx = sx + dj[dir]
# print(sx,Y-sy)

X,Y = map(int,input().split())
sx,sy =map(int,input().split())
T=int(input())

x = (sx + T) //X
y = (sy +T) //Y

if x %2==0:
    res_x=(sx +T) % X
else:
    res_x =X-(sx+T) % X

if y %2==0:
    res_y=(sy +T) % Y
else:
    res_y =Y-(sy+T) % Y
print(res_x,res_y)
