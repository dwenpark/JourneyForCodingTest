import sys

word = sys.stdin.readline()

answer = len(word)
stack = ""
for i in word:
	stack += i
	if len(stack) < 2:
		pass
	elif len(stack) >= 2 and i in ["=", "-"]:
		if stack[-3:-1] in ["c=", "c-", "d-", "s=", "z="]:
			answer += 1
			stack = ""
	elif len(stack) >= 3 and stack[-4:-1] == "dz=":
		answer += 1
		stack = ""

print(answer)