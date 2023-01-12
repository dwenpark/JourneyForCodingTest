import sys

answer = 0
x, y = 1, 1
lst = []
for _ in range(9):
	lst.append(list(map(int, sys.stdin.readline().rstrip().split())))

for i in range(9):
	for j in range(9):
		if lst[i][j] > answer:
			answer = lst[i][j]
			x, y = i+1, j+1

print(answer)
print(x, y)