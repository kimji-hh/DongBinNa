# 재귀함수

def recursive_function(i):
    if i == 100:
        return 
    print(i, '번째 재귀 함수에서', i+1, '번째 재귀 함수를 호출한다.')
    recursive_function(i+1)
    print(i, '번째 재귀 함수를 종료한다.')

recursive_function(1)

# return: 이전 호출문으로 되돌아가라
# 즉, recursive_function(99)를 종료하고 호출했던 
# recursive_function(98)으로 되돌아가라
########################

# 반복문 vs 재귀문

# 반복으로 구현한 n!
def factorial_iterative(n):
    result = 1
    # 1부터 n까지의 수를 차례대로 곱하기
    for i in range(1, n+1):
        result *= i
    return result

# 재귀로 구현한 n!
def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n-1)