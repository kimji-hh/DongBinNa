# 최소한의 거리로 파일 드래그
def solution(wallpaper):
    # 파일있는 좌표
    dx = []
    dy = []
    # wallpaper = 컴퓨터 바탕화면 상태
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == "#":
                dx.append(i)
                dy.append(j)
    
    # S 좌표 찾기. x작은거 and y작은거    x큰거, y큰거
    
    return [min(dx), min(dy), max(dx)+1, max(dy)+1]
