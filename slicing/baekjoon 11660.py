import sys

N, M = map(int, sys.stdin.readline().split())

lst = []
for _ in range(N):
	lst.append(list(map(int, sys.stdin.readline().split())))

tmp = []
for _ in range(M):
	start_i, start_j, end_i, end_j = map(int, sys.stdin.readline().split())
	total = 0
	for i in range(start_i-1, end_i):
		total += sum(lst[i][start_j-1:end_j])
	print(total)