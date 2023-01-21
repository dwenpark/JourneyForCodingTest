import sys
K, N = map(int, sys.stdin.readline().split())

lst = []

for _ in range(K):
    lst.append(int(input()))
lst.sort()

start = 1
end = lst[-1]
cnt, tmp, mid = 0, 0, 0 

while start <= end:
    cnt = 0
    mid = (start + end) // 2

    for i in lst:
        if i >= mid:
            cnt += i // mid

    if cnt >= N:
        if mid > tmp:
            tmp = mid
        start = mid + 1
    else:
        end = mid - 1

print(tmp)