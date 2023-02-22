L = int(input())
N = str(input())

answer = 0

cnt = 0
for i in N:
	tmp = ord(i) - 96
	answer+= (31 ** cnt) * (tmp)
	cnt += 1


print(answer % 1234567891)