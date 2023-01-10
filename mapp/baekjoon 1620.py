import sys

a = list(map(int, sys.stdin.readline().split()))

dict = {}

for i in range(1,a[0]+1):
	tmp = str(sys.stdin.readline().strip())
	dict[tmp] = i
	dict[i] = tmp

for _ in range(a[1]):
	tmp = str(sys.stdin.readline().strip())
	if tmp.isdigit():
		print(dict[int(tmp)])
	else:
		print(dict[tmp])
