import sys

a = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().split()))

answer = []
buffer = []
for i in b:
	if not buffer:
		buffer.append(i)

print(buffer)