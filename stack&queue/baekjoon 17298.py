import sys

a = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().split()))

answer = [-1]
stack = []
for i in b[::-1]:
	if not stack:
		stack.append(i)
	else:
		if stack[-1] >= i:
			stack.append(i)
		else:
			answer.extend([stack[0]] * len(stack))
			stack = []
answer.append(-1)
print(answer)