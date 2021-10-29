# https://programmers.co.kr/learn/courses/30/lessons/12940

def solution(n, m):
    answer = [0,0]
    for i in range(min(n,m),0,-1):
        if not n%i and not m%i:
            answer[0] = i
            break
    for j in range(max(n,m),(n*m)+1):
        if not j%n and not j%m:
            answer[1] = j
            break
    return answer