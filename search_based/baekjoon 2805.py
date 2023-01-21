import sys
N, M = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))

lst.sort()

start = 1
end = lst[-1]

global log, tmp
tmp = 0

while start <= end:
    log = 0
    mid = (start + end) // 2

    for i in lst:
        if i > mid:
            log += (i - mid)

    if log >= M:
        if mid > tmp:
            tmp = mid
        start = mid + 1
    elif log <= M:
        end = mid - 1

print(tmp)