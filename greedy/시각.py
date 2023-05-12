# 시각
# 정수 N이 입력이 되면 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 
# 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램을 작성하라.

n = int(input())
count = 0

h = 60

for j in range(n+1):
    for m in range(h):
        for s in range(60):
            if '3' in str(j) + str(m) + str(s):
                count += 1

print(count)
############

n = int(input())
x, y = 1, 1
# 얼마나 이동할지 계획 입력 받기
plans = input().split()

# L, R, U, D에 따른 이동 방향  
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# 이동 계획을 하나씩 확인
for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    
    # 공간을 벗어난 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    # 이동 수행
    x, y = nx, ny

print(x, y)
