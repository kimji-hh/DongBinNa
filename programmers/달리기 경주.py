# 리스트에서 특정 value를 가지고 find하기 어려우므로 딕셔너리를 사용한다.
# 특정 value(이름)을 호출하면 등수를 변경하는 방식


def solution(players, callings):
    answer = []
    hashmap = dict()
    
    # hashmap에 players 값 넣기. 
    # len(array)하지 않고 바로 넣기 위해 enumerate()사용
    # index와 value(선수이름) 넣기
    for i, v in enumerate(players):
        hashmap[v] = i
    
    # callings 
    for call in callings:
        # pre = call한 선수 이름의 등수 - 1, post = call한 선수 이름의 등수
        pre, post = hashmap[call] - 1,hashmap[call]

        # hashmap, players 모두 교체
        # hashmap은 이름만 들어가야하므로 players를 통해 이름 얻기
        hashmap[players[pre]], hashmap[players[post]] = post, pre # index
        players[pre], players[post] = players[post], players[pre] # 이름값
    return players