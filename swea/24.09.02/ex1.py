def func(x):
    if x==5:
        print(path)
        return

    for i in range(1,5):
        path.append(i)
        func(x+1)
        path.pop()

x=0
path=[]
func(x)
