# 스택(Stack)
# 5, 2, 3, 1 순서로 insert
# -4 -3 -2 -1
# 0 1 2 3 index이다.
# 0 ~ -1 (처음~ 끝 index) 
# 오른쪽부터 pop

# 탐색: 많은 양의 데이터 중 원하는 데이터를 찾는 과정
# 대표적인 탐색 알고리즘 : DFS, BFS

# 자료구조: 데이터를 표현하고 관리하고 처리하기 위한 구조
# 삽입(Push): 데이터 삽입, 삭제(Pop): 데이터 삭제
# 오버플로(Overflow): 넘침, 언더플로(Underflow): 없음

# 스택(Stack): 선입후출(First In Last Out)

# 삽입(5)-삽입(2)-삽입(3)-삽입(7)-삭제()-삽입(1)-삽입(4)-삭제()
stack = []
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack)
print(stack[2])

# 큐(Queue)
# 3, 7, 1, 4 순서로 insert
# -4 -3 -2 -1
# 0 1 2 3 index이다.
# 왼쪽부터 popleft

from collections import deque
# 큐(Queue) 구현을 위해 deque 라이브러리 사용

queue = deque()

# 삽입(5)-삽입(2)-삽입(3)-삽입(7)-삭제()-삽입(1)-삽입(4)-삭제()
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)
queue.reverse()
print(queue)
