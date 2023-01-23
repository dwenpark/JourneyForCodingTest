import sys

N, S = map(int, sys.stdin.readline().split())

lst = list(map(int, sys.stdin.readline().split()))

answer = len(lst)
start = 0
end = 1

if sum(lst) < S:
	print(0)
else:
	while (end <= len(lst) or answer == 1):
		if sum(lst[start:end]) >= S:
			start += 1
			if answer > end - start:
				answer = end - start + 1
		elif sum(lst[start:end]) < S:
			end += 1
	print(answer)