import sys

N, M = map(int, sys.stdin.readline().split())

T = set(list(map(int, sys.stdin.readline().split()))[1:])

meets = []
for i in range(M):
	meets.append(set(list(map(int, sys.stdin.readline().split()))[1:]))

for _ in range(M):
	for meet in meets:
		if T & meet:
			T = T.union(meet)

answer = 0
for meet in meets:
	if not T & meet:
		answer += 1
	
print(answer)