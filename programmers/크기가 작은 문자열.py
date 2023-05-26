def solution(t, p):
  answer = 0
  p_len = len(p)
  t_len = len(t)
  p = int(p)
  for i in range(0,t_len+1-p_len):
      if int(t[i:i+p_len]) <= p:
          answer+=1
  return answer

#########################################
# 내가 작성한 코드
# 작거나 같은 수의 갯수 출력

def solution(t, p):
    answer = 0
    sum_str = ''
    # t에서 p의 길이만큼 나누기
    for div in range(len(t)):
        sum_str = t[div:div + len(p)]
        if len(sum_str) != len(p):
            break
        if int(sum_str) <= int(p):
            answer += 1
        
    return answer

# 소감
# 아. 우선 축하부터… 축하드립니다!
# 처음으로 답지 안보고 맞춘 문제이다. 물론 시간은 아직도 오래 걸린다. ^^
 

