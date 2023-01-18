import sys
N = int(input())

dic = {}
for _ in range(N):
	age, name = sys.stdin.readline().split()
	age = int(age)
	if dic.get(age, False):
			dic[age].append(name)
	else:
		dic[age] = [name]

for key, value in sorted(dic.items()):
	for i in value:
		print(key, i)