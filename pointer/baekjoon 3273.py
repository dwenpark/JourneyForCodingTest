import sys

N = int(sys.stdin.readline())

lst = list(map(int, sys.stdin.readline().split()))
lst.sort()

X = int(sys.stdin.readline())

start = 0
end = N-1

answer = 0

while start < end:
	tmp = lst[start] + lst[end]
	if tmp == X:
		answer += 1
	elif tmp < X:
		start += 1
		continue
	end -= 1

print(answer)