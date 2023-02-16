a = int(input())
b = list(map(int,input().split()))

lst = []
now = 0

if max(b) <= 0:
	print(max(b))
else:
	for i in b:
		if now + i <= 0:
			now = 0
		else:
			now += i
			lst.append(now)
	print(max(lst))