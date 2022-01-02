def solution(s, n):
    answer = ''
    for i in s:
        if i == " ":
            answer += " "
        elif ord(i) >= ord("A") and ord(i) <= ord("Z") and ord(i) + n > ord("Z"):
            answer += chr(ord(i) - 26 + n)
        elif ord(i) >= ord("a") and ord(i) <= ord("z") and ord(i) + n > ord("z"):
            answer += chr(ord(i) - 26 + n)
        else:
            answer += chr(ord(i) + n)
    return answer
