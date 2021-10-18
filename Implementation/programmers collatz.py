# https://programmers.co.kr/learn/courses/30/lessons/12943

def solution(num):
    result = 0
    while num != 1 and result < 500:
        result += 1
        if not num % 2:
            num = num / 2
        else:
            num = num * 3 + 1
    return result if result < 500 else -1