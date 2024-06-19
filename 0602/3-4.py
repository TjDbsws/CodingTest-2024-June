# 2중 반복문 구조 이용하기

n, m = map(int, input().split())

result = 0

for i in range(n): # 한 행씩 실행
    data = list(map(int, input().split())) # 현재 행을 리스트로 저장
    min_value = 10001 # 최소값을 찾기 위해 임의의 값 설정
    for a in data: # 한 행의 요소를 반복
        min_value = min(min_value, a) # 임의의 값으로 설정한 최소값과 요소를 반복하면서 비교 ➜ min_value를 업데이트
    result = max(result, min_value) # 현재 행의 min_value와 result를 비교 ➜ 최소값 중 최대값이 result에 저장

print(result)
