# k는 2 이상의 자연수
# n이 클수록 k로 나누었을 때 많이 줄어든다.

n, k = map(int, input().split())

count = 0

while n >= k :
    # 나누어 떨어지지 않는다면
    while n % k != 0:
        n -= 1
        count += 1

    # 나누어떨어진다면
    n //= k
    count += 1

while n > 1:
    n -= 1
    count += 1

print(count)
