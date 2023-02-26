import sys

N, S = map(int, sys.stdin.readline().split())

lst = list(map(int, sys.stdin.readline().split())) + [0, 0]

start = 0
end = 0
answer = N

total = lst[start]
if sum(lst) < S:
	print(0)
else:
	while end <= N:
		if total < S:
			end += 1
			total += lst[end]
		else:
			answer = min(answer, end - start+1)
			total -= lst[start]
			start += 1
	print(answer)