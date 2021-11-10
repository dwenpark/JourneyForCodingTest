# https://programmers.co.kr/learn/courses/30/lessons/12945#

def solution(n):
    return fibofunc(n) % 1234567

def fibofunc(v):
    fibo = []
    fibo.append(0)
    fibo.append(1)
    fibo.append(1)
    for i in range(3, v+1):
        fibo.append(fibo[i-1] % 1234567 + fibo[i-2] % 1234567)
    return fibo[v]