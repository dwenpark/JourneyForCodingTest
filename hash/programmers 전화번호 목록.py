# https://programmers.co.kr/learn/courses/30/lessons/42577

def solution(phone_book):
    phone_book.sort(reverse=True)
    while len(phone_book) != 1:
        num = phone_book.pop()
        if num == phone_book[-1][:len(num)]:
            return False
    return True