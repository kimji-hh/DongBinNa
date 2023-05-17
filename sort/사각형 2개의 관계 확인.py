# 사각형 두 개 겹치는지 확인
# 4개의 좌표 입력 받기
# ex) 
# 1번째 입력값: (-2, 2), (2, 2)(-2, -2), (2, -2)
# 2번째 입력 값: (3, 2) (-4, 2) (3, -4) (-3, -4)
# 1번째 입력값이 2번째 입력값의 안쪽 or 바깥 or 겹치는지 or 똑같은지 출력
# 입력하신 사각형이 어디에있는지 출력하기


# 1번째 좌표 입력받기
x_m_1 = []
y_m_1 = []


x_m_3_1, y_m_3_1 = map(int, input().split())
x_m_2_1, y_p_2_1 = map(int, input().split())
x_p_1_1, y_p_1_1 = map(int, input().split())
x_p_4_1, y_m_4_1 = map(int, input().split())

x_m_1.append(0)
y_m_1.append(0)

x_m_1.append(x_p_1_1)
y_m_1.append(y_p_1_1)
x_m_1.append(x_m_2_1)
y_m_1.append(y_p_2_1)
x_m_1.append(x_m_3_1)
y_m_1.append(y_m_3_1)
x_m_1.append(x_p_4_1)
y_m_1.append(y_m_4_1)
# 2번재 좌표 입력받기
x_m_2 = []
y_m_2 = []

x_m_3_2, y_m_3_2 = map(int, input().split())
x_m_2_2, y_p_2_2 = map(int, input().split())
x_p_1_2, y_p_1_2 = map(int, input().split())
x_p_4_2, y_m_4_2 = map(int, input().split())

x_m_2.append(0)
y_m_2.append(0)

x_m_2.append(x_p_1_2)
y_m_2.append(y_p_1_2)
x_m_2.append(x_m_2_2)
y_m_2.append(y_p_2_2)
x_m_2.append(x_m_3_2)
y_m_2.append(y_m_3_2)
x_m_2.append(x_p_4_2)
y_m_2.append(y_m_4_2)


# 사분면
array = [0, False, False, False, False]

out = 0
count = 0
# left
while out != 1:
    for i in range(1, 5):
        # 안쪽
        # 사분면 좌표 비교
        if x_m_1[i] < x_m_2[i] or y_m_1[i] < y_m_2[i]:
            count += 1
            array[i] = True
            
        else:
            array[i] = False

        if x_m_1[i] == x_m_2[i] and y_m_1[i] == y_m_2[i]:
            count += 2
            array[i] = True


    if count == 8:
            print("똑같다.")
            out = 1
    if count == 4:
        
            print("안쪽에 있다.")
            out = 1

    elif count < 4:
        print("겹친다")
        out = 1

    elif count == 0:
        print("바깥 쪽이다.")
        out = 1
    
    else:
        break



