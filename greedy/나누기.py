# 1. N에서 1을 뺀다. 2번이 가능하면 2번을 진행한다.
# 2. N을 K로 나눈다.
# N이 17, K가 4

n, k = map(int, input().split())
count = 0
while(n != 1):
    if n % k == 0:
        n = n // k
        count += 1
        continue
    n -= 1
    count += 1

print(count)
