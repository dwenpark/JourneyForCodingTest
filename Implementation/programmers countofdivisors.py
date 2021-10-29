# https://programmers.co.kr/learn/courses/30/lessons/77884

def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        tmp = 0
        for j in range(1, i+1):
            if not i%j:
                tmp += 1
        if tmp % 2:
            answer -= j
        else:
            answer += j
    return answer