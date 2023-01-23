import sys

N = int(input())
lst = list(map(int, sys.stdin.readline().split()))

tmp = sorted(list(set(lst)))
dic= {}

for i in range(len(tmp)):
	dic[tmp[i]] = i

answer = []
for j in lst:
	answer.append(dic[j])

print(*answer)