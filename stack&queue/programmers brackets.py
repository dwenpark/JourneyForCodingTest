# https://programmers.co.kr/learn/courses/30/lessons/12909

from collections import deque

def solution(s):
    q = deque()

    for i in s:
        if i=='(':
            q.append(i)
        else:
            if len(q)==0 or q.pop()==')':
                return False

    if len(q)!=0:
        return False
    return True