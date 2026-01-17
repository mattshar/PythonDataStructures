from collections import deque

q = deque()

q.append(1)      # 
q.append(2)
q.append(3)

item = q.popleft()  
print(item)  # 1