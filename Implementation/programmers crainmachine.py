# https://programmers.co.kr/learn/courses/30/lessons/64061

def solution(board, moves):
    doll = []
    answer = 0
    for move in moves:
        cnt = 0
        while (cnt < len(board[0])):
            if board[cnt][move-1]:
                doll.append(board[cnt][move-1])
                board[cnt][move-1] = 0
                break
            else:
                cnt += 1
        if len(doll) > 1 and doll[-1] == doll[-2]:
            doll.pop(-1)
            doll.pop(-1)
            answer += 2
    return answer