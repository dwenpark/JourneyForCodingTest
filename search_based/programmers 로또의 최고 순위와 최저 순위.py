# https://programmers.co.kr/learn/courses/30/lessons/77484

def solution(lottos, win_nums):
    zero = lottos.count(0)
    cnt  = 0
    for i in lottos:
        if i in win_nums:
            cnt += 1
    return [7-cnt-zero, 7-cnt if zero != 6 else 6] if (cnt+zero >= 2) else [6, 6]
