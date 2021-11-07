# https://programmers.co.kr/learn/courses/30/lessons/81301

def solution(s):
    answer = ""
    words = {"zero" : "0",
            "one" : "1",
            "two" : "2",
            "three" : "3",
            "four" : "4",
            "five" : "5",
            "six" : "6",
            "seven" : "7",
            "eight" : "8",
            "nine" : "9"}
    tmp = ""
    for i in s:
        if i.isdigit():
            answer += i
        else:
            tmp += i
            if tmp in words:
                answer += words[tmp]
                tmp = ""
    return int(answer)