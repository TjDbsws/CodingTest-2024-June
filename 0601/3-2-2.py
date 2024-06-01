# 반복되는 수열을 고려하여 작성하기
# 1. 반복되는 구간 고려하기
# 2. 반복되는 구간이 n에 나누어 떨어지는지 고려하기

# 전체 길이(m)에서 큰 수가 등장하는 횟수 = m // (k + 1)

# 전체 길이에서 반복되는 길이가 나누어떨어지지 않을 때
# 전체 길이에서 반복되는 크기만큼 나눴을 때 나머지만큼 큰 수가 더해짐 = (k + 1) % m

n, m, k = 5, 8, 3
nlist = [2, 4, 5, 4, 6]

first = nlist[n - 1]
second = nlist[n - 2]

# 완성 코드
# 큰 수가 더해지는 횟수
count = m // (k + 1)
count += m % (k + 1)

# 결과 대입
result = count * first
result += (m - count) * second

# 결과 출력
print(result)