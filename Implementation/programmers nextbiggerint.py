# https://programmers.co.kr/learn/courses/30/lessons/12911

def solution(n):
    cnt = n
    while True:
        cnt += 1
        if bin(cnt).count("1") == bin(n).count("1"):
            break
    return cnt