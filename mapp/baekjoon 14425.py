import sys


N, M = map(int, sys.stdin.readline().split())

dic = {}

for i in range(N):
	dic[str(input())] = 1

answer = 0
for i in range(M):
	word = (str(input()))
	if dic.get(word, 0):
		answer += 1

print(answer)