# https://codeup.kr/problem.php?id=1402

a = int(input())
b = input().split(" ")

stack = ""
for i in b[::-1]:
    stack += i + " "
print(stack)