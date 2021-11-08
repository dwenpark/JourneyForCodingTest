# https://programmers.co.kr/learn/courses/30/lessons/12935

def solution(arr):
    if len(arr) < 2:
        return [-1]
    else:
        arr.remove(min(arr))
        return arr