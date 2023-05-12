# 큰 수의 법칙
# 첫 째 줄에 N, M, K 입력 각 자연수는 공백으로 구분
# 둘째 줄에 N개의 자연수가 주어진다. 각 자연수는 공백으로 구분
# 입력으로 주어지는 K <= M
# M: M번 더하기 K: 인덱스가 최대 K번 연속 N: 배열의 크기
# 출력: K번 동일한 수 반복하지 않고 M번 더한 값

# 첫 째 줄에 N, M, K 입력 각 자연수는 공백으로 구분
n, m, k = map(int, input().split()) 

# 둘째 줄에 N개의 자연수가 주어진다. 각 자연수는 공백으로 구분
data = list(map(int, input().split()))
data.sort()
first = data[n-1] # 가장 큰 수
second = data[n-2] # 두 번째로 가장 큰 수

result = 0

# first와 second를 인덱스가 K번 겹치지 않으면서 M번 더한다.
while True:
    # 동일한 인덱스가 K번 겹치지 않으면서    
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1

    if m == 0:
        break
    result += second
    m -= 1

print(result)
#########################
# 숫자 카드 게임
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
