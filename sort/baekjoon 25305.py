a = list(map(int, input().split()))
b = list(map(int, input().split()))

print(sorted(b, reverse=True)[a[1]-1])