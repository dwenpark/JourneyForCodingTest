# https://programmers.co.kr/learn/courses/30/lessons/12899

def solution(n) :
    answer = ""
    cnt = 0
    while True :
        if (n // (3 ** cnt)) >= 1 :
            cnt += 1
            if (n % (3 ** cnt)) == (3 ** (cnt - 1)) * 1 :
                answer += "1"
                n -= (3 ** (cnt - 1)) * 1
            elif (n % (3 ** cnt)) == (3 ** (cnt - 1)) * 2 :
                answer += "2"
                n -= (3 ** (cnt - 1)) * 2
            elif (n % (3 ** cnt)) == 0 :
                answer += "4"
                n -= (3 ** (cnt - 1)) * 3
        else :
            break
    
    return answer[: :-1]