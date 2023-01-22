import sys
N = int(input())

dic = {}
for _ in range(N):
	tmp = str(input())
	if dic.get(len(tmp), 0):
		if not tmp in dic[len(tmp)]:
			dic[len(tmp)].append(tmp)
			dic[len(tmp)].sort()
	else:
		dic[len(tmp)] = [tmp]

for i in sorted(list(dic.keys())):
	for j in dic[i]:
		print(j)