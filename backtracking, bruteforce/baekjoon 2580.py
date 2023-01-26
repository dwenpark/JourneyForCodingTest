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
		
print(div)
while zero:
	for i in zero:
		a , b = i[0], i[1]
		if sdk[a].count(0) == 1:
			sdk[a][b] = 45 - sum(sdk[a])
			div[(b // 3) * 3 + (a // 3)][(a % 3) * 3 + (b % 3)] = sdk[a][b]
			print(i, sdk[a][b], 1)
			zero.remove(i)
		elif [row[b] for row in sdk].count(0) == 1:
			sdk[a][b] = 45 - sum([row[b] for row in sdk])
			div[(b // 3) * 3 + (a // 3)][(a % 3) * 3 + (b % 3)] = sdk[a][b]
			print(i, sdk[a][b], 2)
			zero.remove(i)
		else:
			for k in div:
				if k.count(0) == 1:
					div[(b // 3) * 3 + (a // 3)][(a % 3) * 3 + (b % 3)] = 45 - sum(div[(b // 3) * 3 + (a // 3)])
					sdk[a][b] = div[(b // 3) * 3 + (a // 3)][(a % 3) * 3 + (b % 3)]
					print(i, sdk[a][b], 3)
					zero.remove(i)
					break	

for k in sdk:
	print(*k)
