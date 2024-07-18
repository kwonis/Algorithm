T=input()
ab=list(T)
abc=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S',
     'T','U','V','W','X','Y','Z']
list_1 =[]
# print(abc.index(ab)+1)
for i in range(len(ab)): 
   print(abc.index(ab[i])+1,end=' ')

