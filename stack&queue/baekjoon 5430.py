import sys
from collections import deque

N = int(input())

for _ in range(N):
	p = str(input())
	n = int(input())
	lst = sys.stdin.readline().rstrip()[1:-1].split(',')
	reverse = False
	error = False
	
	if n == 0:
		q = []
	else:
		q = deque(lst)

	for i in p:
		if i == "R":
			if reverse:
				reverse = False
			else:
				reverse = True
		else:
			if len(q) < 1:
				error = True
				break
			if reverse:
				q.pop()
			else:
				q.popleft()

	if error:
		print("error")
	else:
		if reverse:
			q.reverse()
		print("[" + ",".join(q) + "]")