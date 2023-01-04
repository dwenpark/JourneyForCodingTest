tmp = []
for i in range(5):
	tmp.append(int(input()))

print(sum(tmp) // len(tmp))
print(sorted(tmp)[2])