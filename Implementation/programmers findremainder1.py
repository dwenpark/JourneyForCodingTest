def solution(n):
    cnt = 0
    while True:
        cnt += 1
        if n % cnt == 1:
            break
    return cnt