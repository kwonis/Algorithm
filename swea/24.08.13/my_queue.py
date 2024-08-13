N = 10
q=[0]*N
front = -1
rear = -1

rear +=1
q[rear] =1
rear +=1
q[rear] =2
# enqueue(1)
# enqueue(2)

#dequeue()
front+=1
print(q[front])

q2 = []
q2.append(10)
q2.append(20)
q2.pop(0)