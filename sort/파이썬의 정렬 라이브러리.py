# 파이썬의 정렬 라이브러리

# sorted() 소스코드
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

result = sorted(array)
print(result)


# sort() 소스코드
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

array.sort()
print(array)

# sorted, key를 활용한 소스코드
array = [('바나나', 2), ('사과', 5), ('당근', 3)]

def setting(data):
    return data[1]

result = sorted(array, key=setting)
print(result)

# 정렬 라이브러리의 시간 복잡도
# 빅오표기법: O(NlogN)
