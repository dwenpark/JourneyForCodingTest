case = []

while True:
	M = int(input())
	if M == 0:
		break
	else:
		case.append(M)

N = max(case) * 2
lst = [0, 1] + [0] * (N-1)

for i in range(1, N+1):
	n = 1
	cnt = n * i
	while cnt < N+1:
		lst[cnt] += 1
		n += 1
		cnt = n * i

for j in case:
	print(lst[j+1:2*j+1].count(2))