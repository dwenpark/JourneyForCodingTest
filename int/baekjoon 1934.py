import sys

N = int(sys.stdin.readline())

def gcd(x, y):
	if not (y % x):
		return x
	return gcd(y % x, x)

for _ in range(N):
	a, b = map(int,sys.stdin.readline().split())
	print (a * b // gcd(a, b))
