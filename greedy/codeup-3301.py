a      = int(input())
bill   = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
result = 0

while (a!=0) :
    for i in bill:
        if a >= i:
            result += (a//i)
            a %= i

print(result)