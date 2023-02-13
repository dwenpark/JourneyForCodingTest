import sys


N, M = map(int, sys.stdin.readline().split())

dic = {}

for i in range(N):
	dic[str(input())] = 1

answer = []
for i in range(M):
	word = (str(input()))
	if dic.get(word, 0):
		answer.append(word)

answer.sort()
print(len(answer))
for i in answer:
	print(i)