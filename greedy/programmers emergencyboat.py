# https://programmers.co.kr/learn/courses/30/lessons/42885

from collections import deque

def solution(people, limit):
    cnt = 0
    people.sort()
    que = deque(people)
    while len(que):
        if len(que) == 1:
            cnt += 1
            break
        else:
            if que[0] + que[-1] > limit:
                que.pop()
                cnt += 1
            else:
                que.pop()
                que.popleft()
                cnt += 1
    return cnt