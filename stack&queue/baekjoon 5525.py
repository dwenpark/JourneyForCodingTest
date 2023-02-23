import sys

N = int(input())
word = 1 + 2 * N

M = int(input())

S = str(input())

tmp = 0
answer = 0

for i in S:
	if not tmp:
		if i == "I":
			tmp = 1
	else:		
		if tmp % 2 and i == "I":
			tmp = 1
		elif tmp % 2 and i == "O":
			tmp += 1
		elif not tmp % 2 and i == "I":
			tmp += 1
		elif not tmp % 2 and i == "O":
			tmp = 0

	if tmp == word:
		answer += 1
		tmp -= 2

print(answer)