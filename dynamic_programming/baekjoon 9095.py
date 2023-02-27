import sys
N   = int(input())

lst = []
for _ in range(N):
	lst.append(int(input()))

dp = [0] * max(lst)

dp[0] = 1
dp[1] = 2
dp[2] = 4


for i in range(3, max(lst)):
	dp[i] = dp[i-3] + dp[i-2] + dp[i-1]

for i in lst:
	print(dp[i-1])