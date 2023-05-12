#  숫자 카드 게임
# n = 행의 개수, m = 열의 개수
n, m = map(int, input().split())
result = 0

# 한 줄씩 입력받아 확인
for i in range(n):
    data = list(map(int, input().split()))
    min_value = 10001
    for a in data:
        min_value = min(min_value, a)
    result = max(result, min_value)
print(result)
# min()함수: ()안에 들어간 value 중 가장 작은 값
# max()함수: ()안에 들어간 value 중 가장 큰 값  
