import sys
sys.setrecursionlimit(10000)

global graph, cnt

def baechu(m, n, k):
	graph = [[0 for i in range (n)] for i in range (m)]
	for _ in range(k):
			a, b = map(int, sys.stdin.readline().split())
			graph[a][b] = 1
	cnt = 0
	for i in range(m):
		for j in range(n):
			if dfs(i, j, m, n, graph):
				cnt += 1
	return cnt

T = int(input())

def dfs(x, y, m, n, graph):
	if x >= m or y >= n or x <= -1 or y <= -1:
		return False
	if graph[x][y] == 1:
		graph[x][y] = 0
		dfs(x - 1, y, m, n, graph)
		dfs(x, y - 1, m, n, graph)
		dfs(x + 1, y, m, n, graph)
		dfs(x, y + 1, m, n, graph)
		return True
	return False

answer = []
for _ in range(T):
	tmp = list(map(int, sys.stdin.readline().split()))
	answer.append(baechu(tmp[0], tmp[1], tmp[2]))

for _ in answer:
	print(_)