import sys
N = int(sys.stdin.readline())

case = [1, 1, 2] + [0] * N

for i in range(3, N+1):
	case[i] = (case[i-2] + case[i-1]) % 15746

print(case[N])