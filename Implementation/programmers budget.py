# https://programmers.co.kr/learn/courses/30/lessons/12982

def solution(d, budget) :
    d.sort()
    answer = 0
    tmp = 0
    for i in d :
        answer += 1
        tmp += i
        if tmp > budget :
            answer -= 1
            break
        elif tmp == budget :
            break
    
    return answer