import sys
data=[1,2,3,4,5,6,7,8,9]

sdk = []
div = [[],[],[],[],[],[],[],[],[]]
zero = []

for i in range(9):
	tmp = list(map(int, sys.stdin.readline().split()))
	sdk.append(tmp)
	for j, value in enumerate(tmp):
		if value == 0:
			zero.append([i,j])
		div[(i // 3) * 3 + (j // 3)].append(value)

while zero:
	for i in zero:
		a , b = i[0], i[1]
		if sdk[a].count(0) == 1:
			sdk[a][b] = 45 - sum(sdk[a])
			div[(a // 3) * 3 + (b // 3)][(a // 3) * 3 + (b % 3)] = sdk[a][b]
		elif [row[b] for row in sdk].count(0) == 1:
			sdk[a][b] = 45 - sum([row[b] for row in sdk])
			div[(a // 3) * 3 + (b // 3)][(a // 3) * 3 + (b % 3)] = sdk[a][b]
		else:
			for k in div:
				if k.count(0) == 1:
					div[(a // 3) * 3 + (b // 3)][(a // 3) * 3 + (b % 3)] = 45 - sum(k)
					sdk[a][b] = div[(a // 3) * 3 + (b // 3)][(a // 3) * 3 + (b % 3)]
					break
		zero.remove(i)

for k in sdk:
	print(*k)
