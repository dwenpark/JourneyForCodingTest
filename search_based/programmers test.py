# https://programmers.co.kr/learn/courses/30/lessons/42840

def solution(answers):
    supo1 = [1,2,3,4,5]
    supo2 = [2,1,2,3,2,4,2,5]
    supo3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    for i in range(len(answers)):
        if supo1[i%len(supo1)] == answers[i]:
            score[0] += 1
        if supo2[i%len(supo2)] == answers[i]:
            score[1] += 1
        if supo3[i%len(supo3)] == answers[i]:
            score[2] += 1
    maxscore = max(score)
    answer = []
    for j in range(3):
        if score[j] == maxscore:
            answer.append(j+1)
    return answer