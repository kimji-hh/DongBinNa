def solution(food):
    answer = ''
    arr, arr2 = [], []
    for i in range(len(food)):
        if food[i] < 2:
            continue
        for _ in range(food[i] // 2):
            arr.append(i)
            arr2.append(i)
    arr2.sort(reverse=True)
    arr.append(0)
    for i in arr2:
        arr.append(i)
    for j in arr:
        answer += str(j)
    return answer