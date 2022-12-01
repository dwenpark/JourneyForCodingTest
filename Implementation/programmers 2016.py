# https://programmers.co.kr/learn/courses/30/lessons/12901
month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def solution(a, b):
    days = sum(month[0:int(a)-1]) + b
    if days % 7 == 0:
        return "THU"
    elif days % 7 == 1:
        return "FRI"
    elif days % 7 == 2:
        return "SAT"
    elif days % 7 == 3:
        return "SUN"
    elif days % 7 == 4:
        return "MON"
    elif days % 7 == 5:
        return "TUE"
    elif days % 7 == 6:
        return "WED"
