# https://codeup.kr/problem.php?id=3117

K     = int(input())
stack = []

for i in range(0, K):
    b = int(input())
    if b:
        stack.append(b)
    else:
        stack.pop()

print(sum(stack))