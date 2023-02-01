import sys

N = int(sys.stdin.readline())

tmp = []
for _ in range(N):
	tmp.append(int(sys.stdin.readline()))

tmp = sorted(tmp)

dict = {}
for i in range(2, tmp[0]+1):
	dict[i] = tmp[0] % i

for k in tmp[1::]:
	lst = list(dict)
	for j in lst:
		if k % j != dict[j]:
			dict.pop(j)

print(*lst)