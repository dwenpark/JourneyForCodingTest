# https://programmers.co.kr/learn/courses/30/lessons/12916

def solution(s):
    p_count = s.count('p') + s.count('P')
    y_count = s.count('y') + s.count('Y')
    return True if p_count == y_count else False