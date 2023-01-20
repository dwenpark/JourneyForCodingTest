import sys
N = int(input())

lst = []
dp = []

for x in range(N):
	lst.append(list(map(int, sys.stdin.readline().split())))
	dp.append([0] * (x+1))

for i in range(N-1):
	for j in range(i+1):
		if i == 0:
			dp[i+1][j] = lst[i][j] + lst[i+1][j]
			dp[i+1][j+1] = lst[i][j] + lst[i+1][j+1]
		else:
			if dp[i+1][j] < dp[i][j] + lst[i+1][j]:
				dp[i+1][j] = dp[i][j] + lst[i+1][j]
			dp[i+1][j+1] = dp[i][j] + lst[i+1][j+1]

if N == 1:
	print(lst[0][0])
else:
	print(max(dp[N-1]))