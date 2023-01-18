import sys
N = int(input())

dic = {}
for _ in range(N):
	age, name = sys.stdin.readline().split()
	age = int(age)
	try:
		if dic[age]:
			dic[age].append(name)
	except:
		dic[age] = [name]

for key, value in sorted(dic.items()):
	for i in value:
		print(key, i)