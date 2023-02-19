import sys

N, M = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))

sum_lst = [0] * (N+1)
tmp = 0
for i in range(N):
	tmp += lst[i]
	sum_lst[i+1] = tmp

for _ in range(M):
	I, J = map(int, sys.stdin.readline().split())
	print(sum_lst[J] - sum_lst[I-1])