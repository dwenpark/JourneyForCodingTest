import sys
data=[1,2,3,4,5,6,7,8,9]

sdk = []
zero = []
for i in range(9):
	tmp = list(map(int, sys.stdin.readline().split()))
	sdk.append(tmp)
	[zero.append([i, j]) for j, value in enumerate(tmp) if value == 0]

while zero:
	for i in zero:
		a , b = i[0], i[1]
		if sdk[a].count(0) == 1:
			sdk[a][b] = 45 - sum(sdk[a])
			zero.remove(i)
		elif [row[b] for row in sdk].count(0) == 1:
			sdk[a][b] = 45 - sum([row[b] for row in sdk])
			zero.remove(i)

		if sdk[a].count(0) >= 2 or [row[b] for row in sdk].count(0) >= 2:
			for n in data:
				if (n not in sdk[a]) and (n not in [row[b] for row in sdk]):
					sdk[a][b] = n
					zero.remove(i)

for k in sdk:
	print(*k)
