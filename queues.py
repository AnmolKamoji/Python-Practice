from collections import deque
queue = deque()
queue.append(1)
queue.appendleft(2)
queue.pop()
queue.appendleft(3)
queue.appendleft(4)
queue.popleft()
print(queue) 
