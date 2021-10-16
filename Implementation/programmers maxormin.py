# https://programmers.co.kr/learn/courses/30/lessons/12939

def solution(s):
    lst = [int(i) for i in s.split(" ")]
    return str(sorted(lst)[0]) + " " + str(sorted(lst, reverse = True)[0])