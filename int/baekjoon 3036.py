import sys

def gcd(x, y):
	if not (y % x):
		return x
	return gcd(y % x, x)

N = int(input())
lst = list(map(int,sys.stdin.readline().split()))

for i in lst[1::]:
	gcd(lst[0], i)
	print(str(lst[0]//gcd(lst[0], i)) + "/" + str(i//gcd(lst[0], i)))
