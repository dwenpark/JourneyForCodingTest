import sys
M, N = map(int, sys.stdin.readline().split())

lst = [0] * (N+1)
answer =[]
for i in range(1, N+1):
	if lst[i] == 1 and i >= M and i <= N:
		answer.append(i)
	n = 1
	cnt = n * i
	while cnt < N+1:
		lst[cnt] += 1
		n += 1
		cnt = n * i

for i in answer:
	print(i)