# BFS 미로찾기
from collections import deque

n,m = input("").split(" ")

graph = []

for i in range(int(n)):
	graph.append(list(map(int,input("list : "))))

print(graph)
