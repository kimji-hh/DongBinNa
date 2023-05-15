# 퀵 정렬(Quick Sort)
# 기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸기

# 피벗(Pivot)
# 큰 숫자와 작은 숫자를 교환할 때, 교환하기 위한 '기준'

# 진행 절차
# 1. 리스트에서 첫 번째 데이터를 피벗으로 정한다.
# 2. 피벗을 설정한 후, 리스트 왼쪽에서부터 피벗보다 큰 데이터를 찾고, 오른쪽에서부터 피벗보다 작은 데이터를 찾는다.
# 3. 그다음 큰 데이터와 작은 데이터의 위치를 서로 교환해준다.

# 단점
# 평균적으로 시간 복잡도가 O(NlogN)이지만 최악의 경우 시간 복잡도가 O(N^2)이다.

# 퀵 정렬 소스코드1
# 퀵 정렬

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end: # 원소가 1개인 경우 종료
        return
    pivot = start # 피벗은 첫 번째 원소
    left = start + 1
    right = end
    while left <= right:
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while left <= right:
            left += 1
        
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while right > start and array[start] >= array[pivot]:
            right -= 1
        if left > right: # 엇갈렸다면 작은 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]
        else: # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[left], array[right] = array[right], array[left]
    
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)

quick_sort(array, 0, len(array) - 1)
print(array)