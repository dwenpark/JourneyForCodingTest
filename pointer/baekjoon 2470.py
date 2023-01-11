import sys

N = int(sys.stdin.readline())

lst = list(map(int, sys.stdin.readline().split()))
lst.sort()

start = 0
end = N-1

answer = [lst[start], lst[end]]

while start < end:
	tmp = lst[start] + lst[end]
	if abs(tmp) < abs(sum(answer)):
		answer = [lst[start], lst[end]]
	
	if tmp > 0:
		end -= 1
	elif tmp <= 0:
		start += 1

print(*answer)