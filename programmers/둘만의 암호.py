def solution(s, skip, index):
    answer = ''

    for i in s:
        count = 0 # index 만큼 뛰기
        ord_word = ord(i) # 문자 i를 숫자로 변환

        while count != index:
            ord_word += 1

            if ord_word > ord('z'):
                ord_word = ord_word - ord('z') + ord('a') - 1
            if chr(ord_word) in skip:  
                continue
            count += 1
        answer += chr(ord_word)
    
    return answer

# 소감
# 애 먹은 이유는 substring in string 비교를 i로 할 수 없었다. ord_word가 while 문에서 값이 달라지기 때문이다. 
