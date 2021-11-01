# https://programmers.co.kr/learn/courses/30/lessons/12930

def solution(s):
    words = s.split(" ")
    lst = []
    for i in words:
        tmp = ""
        for j in range(len(i)):
            if not j % 2:
                tmp += i[j].upper()
            else:
                tmp += i[j].lower()
        lst.append(tmp)
    return " ".join(lst)