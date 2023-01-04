# 음료수 얼려먹기

n,m = input("").split(",")

graph = []

for i in range(int(n)):
	graph.append(list(map(int,input("list : "))))

print(graph)

def dfs(x, y):
	if x <= -1 or y <=-1 or x >=int(n) or y >=int(m):
		return False
	elif graph[x][y] == 0:
		graph[x][y] = 1
		dfs(x-1, y)
		dfs(x, y-1)
		dfs(x+1, y)
		dfs(x, y+1)
		return True
	else:
		return False

result = 0
for i in range(int(n)):
	for j in range(int(m)):
		if dfs(i,j) == True:
			result += 1

print(result)