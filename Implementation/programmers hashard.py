# https://programmers.co.kr/learn/courses/30/lessons/12947

def solution(x):
    total = sum([int(i) for i in str(x)])
    return False if x % total else True