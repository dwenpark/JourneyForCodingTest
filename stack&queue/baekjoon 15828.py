import sys
from collections import deque

K = int(sys.stdin.readline())

q = deque()
while True:
	tmp = int(sys.stdin.readline())
	if tmp == -1:
		break
	else:
		if tmp == 0:
			q.popleft()
		elif len(q) < K:
			q.append(tmp)

if q:
    print(*q)
else: 
    print("empty")