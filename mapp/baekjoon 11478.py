import sys

s = str(input())

n = 1

dic = {}
answer = 0
while n <= len(s):
	for i in range(len(s)-n+1):
		tmp = dic.get(s[i:i+n],0)
		if not tmp:
			dic[s[i:i+n]] = 1
			answer += 1
	n += 1

print(answer)