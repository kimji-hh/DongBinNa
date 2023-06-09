def solution(k, score):
    arr1 = []; arr2 = [];
        
    # arr1 = 발표 점수
    # arr2 = min 발표 점수
    
    count = k
    for i in score:
        if count == 0:
            if i > min(arr1):
                arr1.sort(reverse=True)
                arr1.pop()
                count = 1
            else:
                arr2.append(min(arr1))
                continue
        arr1.append(i)
        arr2.append(min(arr1))
        count -= 1
    
    return arr2

