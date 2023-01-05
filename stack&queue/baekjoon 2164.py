from collections import deque

N = int(input())

a = deque(range(1,N+1))

for _ in range(N-1):
	a.popleft()
	tmp = a.popleft()
	a.append(tmp)

print(list(a)[0])