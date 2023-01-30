
import sys

a = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().split()))

answer = []
stack = []
for i in range(a-1, -1, -1):
	while stack:
		if stack[-1] > b[i]:
			answer.append(stack[-1])
			stack.append(b[i])
			break
		else:
			stack.pop()
	if not stack:
		answer.append(-1)
		stack.append(b[i])

print(*answer[::-1])