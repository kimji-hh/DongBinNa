def solution(park, routes):
    # 위치 index
    x = 0
    y = 0 
    
    # 시작 위치 찾기
    for i in range(len(park)):
        for j in range(len(park[i])):
            if park[i][j] == 'S':
                x = i
                y = j
                break
    
    # 이동
    dx = [-1, 1, 0, 0]  # 서쪽, 동쪽, 북쪽, 남쪽의 x 방향 이동
    dy = [0, 0, -1, 1]  # 서쪽, 동쪽, 북쪽, 남쪽의 y 방향 이동
    direction = ['N', 'S', 'W', 'E']  # 방향 배열
    
    for route in routes:
        # 위치 초기화
        xx = x
        yy = y
        # 이동 - 장애물이 있거나 공원을 벗어나면 명령 무시
        for step in range(int(route[2])):
            index = direction.index(route[0])  # 현재 방향의 인덱스 가져오기
            nx = xx + dx[index]
            ny = yy + dy[index]
            
            # 이동할 곳이 공원 범위 내이고 장애물이 아닌지 확인
            if 0 <= nx < len(park) and 0 <= ny < len(park[0]) and park[nx][ny] != 'X':
                xx = nx
                yy = ny
                if step == int(route[2])-1:
                    x = xx  # step만큼 움직였으면 위치 초기화
                    y = yy
                    
    return [x, y]
