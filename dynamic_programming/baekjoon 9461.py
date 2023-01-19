import sys
N = int(input())

case = [1] * 3 + [0] * 97

lst = []
for _ in range(N):
	lst.append(int(input()))

for i in range(2, max(lst)):
	case[i] = case[i-3] + case[i-2]

for j in lst:
	print(case[j-1])