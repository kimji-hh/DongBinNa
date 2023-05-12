# 음료수 얼려 먹기
# 첫 번째 줄에 얼음 틀의 세로 길이 N과  가로 길이 M이 주어진다.
# 이때 구멍이 뚫려있는 부분은 0, 그렇지 않은 부분은 1이다.
# 한 번에 만들 수 있는 아이스크림의 개수를 출력한다.

# 1. 특정한 지점의 주변에 상, 하, 좌, 우를 살펴본 뒤 주변 지점 중에서 값이 '0'
# 이면서 아직 방문하지 않은 지점이 있다면 해당 지점을 방문한다.
# 2. 방문한 지점에서 다시 상, 하, 좌, 우를 살펴보며 방문을 다시 진행하면
# 연결된 모든 지점을 방문할 수 있다.
# 1~2번의 과정을 모든 노드에 반복하며 방문하지 않은 지점의 수를 센다.

# N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력 받기
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
        
# dfs로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        # 해당 노드 방문 처리
        graph[x][y] = 1
        # 상, 하, 좌, 우의 위치도 모두 재귀적으로 호출
        dfs[x - 1, y]
        dfs[x, y - 1]
        dfs[x + 1, y]
        dfs[x, y + 1]
        return True  # 0이라면 True 반환
    return False # 1이면 False 반환

# 모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 dfs 수행
        if dfs(i, j) == True:   # 0이면
            result += 1

print(result) # 정답 출력
