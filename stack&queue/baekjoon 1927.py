import sys
from heapq import heappop, heappush

heap = []

N = int(input())

for _ in range(N):
	tmp = int(sys.stdin.readline())
	if tmp == 0:
		try:
			print(heappop(heap))
		except:
			print(0)
	else:
		heappush(heap, tmp)