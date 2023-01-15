import sys
n = int(input())

graph = []
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

cnt = 0

def dfs(x, y):
	global cnt
	if x >= n or y >= n or x <= -1 or y <= -1:
		return False
	if graph[x][y] == 1:
		cnt += 1
		graph[x][y] = 0
		dfs(x - 1, y)
		dfs(x, y - 1)
		dfs(x + 1, y)
		dfs(x, y + 1)
		return True
	return False

lst = []
for i in range(n):
	for j in range(n):
		if dfs(i, j) and cnt:
			lst.append(cnt)
			cnt = 0

print(len(lst))		
for i in sorted(lst):
	print(i)