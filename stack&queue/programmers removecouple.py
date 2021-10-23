# https://programmers.co.kr/learn/courses/30/lessons/12973

def solution(s) :
    answer = [1]
    for i in s :
        if i == answer[-1] :
            answer.pop()
        else :
            answer.append(i)
    
    return 1 if len(answer) == 1 else 0