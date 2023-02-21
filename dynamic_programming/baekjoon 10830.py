import sys

N, B = map(int, sys.stdin.readline().split())


def matrix(arr1, arr2):
	n = len(arr1)
	answer = [[0] * n for _ in range(n)]
	for i in range(n):
		for j in range(n):
			for k in range(n):
				answer[i][j] += (arr1[i][k] * arr2[k][j])
				answer[i][j] %= 1000
	return answer

lst = []

for _ in range(N):
	lst.append(list(map(int, sys.stdin.readline().split())))

if B == 1:
	answer = lst
	n = len(answer)
	for i in range(n):
		for j in range(n):
			for k in range(n):
				answer[i][j] %= 1000
				
else:
	binary = format(B, 'b')

	dynamic_lst = [lst]
	for j in range(len(binary)-1):
		dynamic_lst.append(matrix(dynamic_lst[j], dynamic_lst[j]))

	answer_lst = list(binary)[::-1]
	answer_lst.pop()
	answer = dynamic_lst[-1]

	tmp = 0
	for i in answer_lst:
		if i == "1":
			answer = matrix(answer, dynamic_lst[tmp])
		tmp += 1

for line in answer:
		print (' '.join(map(str, line)))