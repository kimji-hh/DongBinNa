# 9h 40m start
# 추월한 선수의 이름을 부른다.
# 1등부터 3등까지

# players = 선수들의 이름이 1등부터 순서대로 담긴 문자열 배열
# callings = 해설진이 부른 추월한 선수 이름
# 경주가 끝났을때 선수들의 이름을 1등부터 순서대로 배열에 담아 return 하는 solution 함수

def solution(players, callings):
    answer = []
    # players 조건(알파벳 소문자)
    for i in range(len(players)):
        if players[i].isupper() == True:
            players[i] = players[i].lower() 
            print(players[i])
        for j in range(i + 1, len(players)):
            if players[i] == players[j]:
                return
        
        if len(players[i]) < 3 or len(players[i]) > 10:
            break
# callings 이름 불린 애는 이전 애와 자리 바꾸기
    for i in range(len(callings)):
        if len(callings[i]) < 2 or len(callings[i]) > 1000000:
            return
        
        if callings[i] not in players:
            return

        for j in range(1, len(players)):
            if callings[i] == players[j]:
                players[j], players[j-1] = players[j-1], players[j]
        
    return players


