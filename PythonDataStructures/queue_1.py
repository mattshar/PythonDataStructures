from collections import deque

q = deque()

q.append(1)      # 
q.append(2)
q.append(3)

q.extend([4, 5, 6])
q.extendleft([-2, -1])

first = q.popleft()
last = q.pop()

q.rotate(2)
q.rotate(-1)

q.insert(2, 99)
q.remove(3)

length = len(q)
contains = 4 in q

print(first)
print(last)
print(length)
print(contains)
print(q)