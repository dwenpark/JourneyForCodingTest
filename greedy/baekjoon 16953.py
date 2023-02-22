import sys
A, B = map(int, sys.stdin.readline().split())

answer = 1

while (A < B):
	if B % 2:
		if str(B)[-1] == "1":
			B = int(str(B)[:-1])
		else:
			break
	else:
		B = B // 2
	answer += 1

if A == B:
	print(answer)
else:
	print(-1)