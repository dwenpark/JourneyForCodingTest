import sys

sys.stdin.readline()
a = list(map(int, sys.stdin.readline().split()))

sys.stdin.readline()
b = list(map(int, sys.stdin.readline().split()))

tmp = {}
answer = []
for j in a:
	tmp[j] = 1

for i in b:
	try:
		if tmp[i]:
			answer.append(1)
	except:
		answer.append(0)

print(*answer)