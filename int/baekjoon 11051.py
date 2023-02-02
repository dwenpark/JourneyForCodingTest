import sys

N, K = map(int, sys.stdin.readline().split())
lst = [1] * (N+1)

for i in range(1, N+1):
	lst[i] = lst[i-1] * (i)

print((lst[N] // (lst[K] * lst[N-K])) % 10007)