def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    length = len(score) - (len(score) % m)
    min_score = k
    count = m
    for i in range(length):
        count -= 1
        if min_score > score[i]:
            min_score = score[i]
        # 반복이 끝나서 다시 안올라갈 때는 실행X
        if count == 0:
            answer += (min_score * m)
            min_score = k
            count = m
    return answer