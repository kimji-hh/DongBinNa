# 삽입 정렬(Insertion Sort)
# index[0]을 index[1]과 비교하여 왼쪽 or 오른쪽 삽입
array = [7, 5, 9, 0, 3, 1, 6, 1, 4, 8]

for i in range(1, len(array)): 
    for j in range(i, 0, -1): # 앞에 애들 포함 비교하기 위해 -1
        # 인덱스 i부터 1까지 감소하며 반복하는 문법
        if array[j] < array[j - 1]: # 한 칸씩 왼쪽으로 이동
            array[j], array[j - 1] = array[j - 1], array[j]

        else: # 자기보다 작은 데이터를 만나면 그 위치에서 멈춤
            break
print(array)

# range(start, end, step)
# step에 -1이 들어간 경우, start 인덱스부터 end+1 인덱스까지 -1만큼 감소한다.

# range(i, 0, -1)이면, i부터 1까지 -1만큼 감소

# 삽입정렬의 시간 복잡도
# 빅오표기법: O(N^2)
