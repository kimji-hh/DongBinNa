def solution(number, limit, power):
    count = 0
    result = 0
    k = -1
    for i in range(1, number + 1):
        # 제곱근까지만 범위 설정
        for j in range(1, int(i**(1/2)) + 1):
            if i % j == 0:
                count += 1
                # 제곱이 되는 약수 중복 방지
                if j**2 != i:
                    count += 1
            
        if count > limit:
            result += power
        else:
            result += count
        count = 0
    return result