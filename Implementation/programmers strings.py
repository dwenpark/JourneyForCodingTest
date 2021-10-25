# https://programmers.co.kr/learn/courses/30/lessons/12918

def solution(s):
    try:
        if (len(s) == 6 or len(s) ==4) and s.isdigit():
            return True
        else:
            return False
    except:
        return False