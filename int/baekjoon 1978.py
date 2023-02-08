import sys

N = int(input())
k = sorted(list(map(int, sys.stdin.readline().split())))

lst = [0] * (k[-1]+1)
for i in range(1, k[-1]+1):
	n = 1
	cnt = n * i
	while cnt < k[-1]+1:
		lst[cnt] += 1
		n += 1
		cnt = n * i
		
answer = 0
for j in k:
	if lst[j] == 2:
		answer += 1

print(answer)