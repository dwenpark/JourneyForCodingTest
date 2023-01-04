K = int(input())

lst = []
for i in range(K):
	a = int(input())
	if a == 0:
		lst.pop()
	else:
		lst.append(a)

print(sum(lst))