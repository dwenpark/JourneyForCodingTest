T = str(input())
bomb = str(input())

tmp = []
for i in T:
	tmp.append(i)
	if len(tmp) >= len(bomb):
		if tmp[-len(bomb):] == list(bomb):
			del tmp[-len(bomb):]
			
if tmp:
	print("".join(tmp))
else:
	print("FRULA")