def solution(cards1, cards2, goal):
    # 1. 순서 파악

   
    answer = []
    i = j = 0
    # goal에 해당하는 cards1 
    for check in goal:
        if i < len(cards1) and cards1[i] == check:
            answer.append(check)
            i += 1

        if j < len(cards2) and cards2[j] == check:
            answer.append(check)
            j += 1

    if answer == goal:
        return 'Yes'
    else:
        return 'No'                     




