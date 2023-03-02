import sys

n, m = map(int, sys.stdin.readline().split())

lst = [0] * n

total = 1
for i in range(n):
	total *= i+1
	lst[i] = total


print(lst[n-1]//(lst[n-m-1]*lst[m-1]))