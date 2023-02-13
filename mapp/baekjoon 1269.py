import sys


N, M = map(int, sys.stdin.readline().split())

dic = {}

for i in list(map(int, sys.stdin.readline().split())):
	dic[i] = 1

answer = 0
for j in list(map(int, sys.stdin.readline().split())):
	if dic.get(j, 0):
		answer += 1


print(N + M - (2 * answer))