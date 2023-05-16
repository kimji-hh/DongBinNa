# 위에서 아래로
# 첫째 줄에 수열에 속해 있는 수의 개수 N이 주어진다.
# 둘째 줄부터 N+1번째 줄까지 N개의 수가 입력된다.
# 입력으로 주어진 수열이 내림차순으로 정렬되누 결과를 공백으로 구분하여
# 출력된다. 동일한 수의 순서는 자유롭게 출력해도 괜찮다.

# N을 입력받기
n = int(input())

# N개의 정수를 입력받아 리스트에 저장
array = []
for i in range(n):
    array.append(int(input()))

# 파이썬 기본 정렬 라이브러리를 이용하여 정렬 수행
array = sorted(array, reverse=True)

# 정렬이 수행된 결과를 출력
for i in array:
    print(i, end=' ')
    