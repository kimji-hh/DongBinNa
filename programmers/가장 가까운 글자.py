def solution(s):
    answer = []
    check = []
    for i in range(len(s)):
        count = 0
        if s[i] in check:
            answer.append(i - check.index(s[i])) 
            check[check.index(s[i])] = 0
            check += s[i]
        else:
            answer.append(-1)
            check.append(s[i])
    return answer
