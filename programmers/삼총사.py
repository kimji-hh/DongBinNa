def solution(number):
    result = 0
    sum = 0
    for i in range(0, len(number) - 2):
        for j in range(i + 1, len(number) - 1):
            for k in range(j + 1, len(number)):
                sum = number[i] + number[j] + number[k]
                if sum == 0 and i != j != k:
                    result += 1
    return result