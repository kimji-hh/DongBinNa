# 선택정렬(Selection Sort)
# 가장 맨 앞 index[1]와 index[2]~index[n]까지의 작은 수와 교환하여 정렬
# 다른 알고리즘과 비교했을 때 매우 비효율적이다.
# 다만 특정 리스트에서 가장 작은 데이터를 찾는 일이 코딩테스트에서 잦다.

array = [7, 5, 9, 0, 3, 1, 6, 1, 4, 8]

for i in range(len(array)):
    min = i
    for j in range(len(array)):
        if array[min] > array[j]:
            min = j
    array[i], array[min] = array[i], array[min]

print(array)

# 스와프
# array[0], array[1] = array[1], array[0]


# (N-1)번 만큼 가장 작은 수를 찾아서 맨 앞으로 보내야 한다.
# 또한, 매번 가장 작은 수를 찾기 위해 비교 연산이 필요하다.
# N + (N-1)+ (N-2) + ... + 2로 볼 수 있다.
# N * (N+1) / 2의 연산을 수행한다고 가정하자.
# (N^2 + N) / 2는 빅오표기법으로 O(N^2) 이다.

# 파이썬에 내장된 기본 정렬 라이브러리는 내부적으로 C언어 기반이여서 빠르게 동작한다.

# 선택정렬의 시간 복잡도
# 빅오표기법: O(N^2)
