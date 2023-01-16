N = int(input())

start = N - len(str(N)) * 9
if start <= 0:
	start = 1
	
while start <= N:
	tmp = 0
	for i in range(len(str(start))):
		tmp += int(str(start)[i])

	if start + tmp == N:
		break
	else:
		start += 1

if start > N:
	print(0)
else:
	print(start)