import sys
N = int(input())

dp = {0: 0, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1}

for _ in range(N-1):
	new_dp = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
	for i in range(10):
		if i == 0:
			new_dp[i+1] += dp[i]
		elif i == 9:
			new_dp[i-1] += dp[i]
		else:
			new_dp[i+1] += dp[i]
			new_dp[i-1] += dp[i]
	dp = new_dp

print(sum(dp.values())%1000000000)