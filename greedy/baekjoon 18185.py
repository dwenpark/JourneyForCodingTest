import sys
N, K = map(int, sys.stdin.readline().split())

lst = []
for _ in range(N):
	lst.append(int(input()))

lst.sort(reverse=True)
answer = 0

for i in lst:
	if K >= i:
		answer += K // i
		K = K % i

print(answer)