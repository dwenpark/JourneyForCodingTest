# https://codeup.kr/problem.php?id=2628

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort()

if (((b[0] > a[0]) & (b[0] < a[1])) & (b[1] > a[1])) or (((a[0] > b[0]) & (a[0] < b[1])) & (a[1] > b[1])):
    print("cross")
else:
    print("not cross")