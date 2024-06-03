# min() 이용하기
n, m = map(int, input().split())

result = 0
min_value=0

for i in range(n) : # 행만큼 반복
    data = list(map(int, input().split())) # 입력된 행을 리스트 형태로 저장
    min_value = min(data) # 행 중에서 가장 작은 값 찾기
    result = max(data)

print(min_value)
