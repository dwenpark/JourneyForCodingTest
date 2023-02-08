M = int(input())
N = int(input())

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

if answer:
	print(sum(answer))
	print(answer[0])
else:
	print(-1)