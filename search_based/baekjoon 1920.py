import sys
N = int(input())
a = sorted(list(map(int, sys.stdin.readline().split())))

M = int(input())
b = list(map(int, sys.stdin.readline().split()))

for i in b:
    answer = 0
    start, end = 0, N - 1
    while start <= end:
        mid = (start + end) // 2
        if a[mid] < i:
            start = mid + 1
        elif a[mid] > i:
            end = mid - 1
        else:
            answer = 1
            break
    print(answer)
