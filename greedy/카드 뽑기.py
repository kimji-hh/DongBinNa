# N X M 형태로 카드들이 놓여있다. N= 행의 개수, M=열의 개수
# 먼저 뽑고자 하는 카드가 포함되어있는 행을 선택
# 그다음 선택된 행에 포함된 카드들 중 가장 숫자가 낮은 카드를 뽑기
# 따라서 처음에 카드를 골라낼 행을 선택할 때, 이후에 해당 행에서 가장 숫자가 낮은 카드를
# 뽑을 것을 고려하여 최종적으로 가장 높은 숫자의 카드를 뽑을 수 있도록 전략을 세운다.

# N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())
result = 0
# 한 줄씩 입력받아 확인
min = 10001
for j in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    # 가장 작은 수 중 가장 큰 수 찾기
    result = max(result, min_value)

print(result)