def solution(keymap, targets):
    answer = []
    for target in targets:
        minkey = 0 # target을 작성하기 위한 총 횟수
        
        for i in target: # target 문자열 하나씩 눌러야하는 횟수 계산하기
            c = 101 # 100번까지 가능하므로 101을 max로 초기화
            flag = False # 존재하는지 확인하는 flag
            for k in keymap:
                key = k.find(i)
                if key == -1: # k에 존재하지 않으면 continue
                    continue
                c = min(key+1, c) # k에 존재하면 key+1과 c 중 작은 값으로 c 설정
                flag = True # 해당 문자열 존재함으로 flag 표시
                
            if flag: # True이면 minkey에 누적
                minkey += c
            else: # 그렇지 않으면 keymap에 없는 문자이므로 answer에 -1 추가
                answer.append(-1)
                break
        else: # for-else 구문: for문이 온전하게 종료되면 minkey를 answer에 추가
            answer.append(minkey) 
            
    return answer

######################################
# 내가 작성한 코드
def solution(keymap, targets):
    answer = []
    #  targets에서 문자 하나씩 출력
    for tg in targets:
        result = 0
        for t in tg:
            min_value = 101
            flag = False
            # keymap과 맞는지 비교
            for km in keymap:
                key = km.find(t)
                if key != -1 : # ==이면 둘다 고려하게 됨.
                    min_value = min(min_value, key + 1)
                    flag = True
                else:
                    continue
                
            # targes에서 A가 일치할 때
            if flag:
                result += min_value
            # 일치한 것이 없을 때
            else:
                answer.append(-1)
                break
        else:
            answer.append(result)
    return answer

# 소감
# 변수 초기화 중요하다. 
# 선언 위치 중요하다.
# 조건문 걸때는 else일 경우, 다음 문으로 못 넘어가게 continue 혹은 break 필수
