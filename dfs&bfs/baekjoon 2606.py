import sys
m = int(input())
n = int(input())

dic = {}

for i in range(1, m+1):
	dic[i] = []

for _ in range(n):
	a, b = map(int, sys.stdin.readline().split())
	dic[a].append(b)
	dic[b].append(a)

need = [1]
been = []

answer = -1
while need:
	target = need.pop()
	if target in been:
		pass
	else:
		answer += 1
		been.append(target)
		tmp = dic.get(target, 0)
		if tmp:
			for i in tmp:
				if i not in been:
					need.append(i)

print(answer)