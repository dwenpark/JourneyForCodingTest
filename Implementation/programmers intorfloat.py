# https://programmers.co.kr/learn/courses/30/lessons/12934

def solution(n):
    if not (n ** (1/2)) - int((n ** (1/2))):
        return (n**(1/2) + 1)**2
    else:
        return -1