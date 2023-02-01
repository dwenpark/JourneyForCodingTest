import sys

def gcd(x, y):
	if not (y % x):
		return x
	return gcd(y % x, x)

a, b = map(int,sys.stdin.readline().split())
print(gcd(a, b))
print(a * b // gcd(a, b))
