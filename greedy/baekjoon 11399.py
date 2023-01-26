import sys
N = int(input())
lst = list(map(int, sys.stdin.readline().split()))
lst.sort(reverse=True)

answer = 0
for i in range(N):
	answer += lst[i] * (i+1)

print(answer)