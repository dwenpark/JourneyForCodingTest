T = int(input())

for i in range(T):
	string = str(input())
	if len(string) % 2 == 1:
		print("NO")
	else:
		tmp = []
		for i in string:
			tmp.append(i)
			if len(tmp) >= 2:
				if tmp[-1] == ")" and tmp[-2] == "(":
					tmp.pop()
					tmp.pop()
		if tmp:
			print("NO")
		else:
			print("YES")