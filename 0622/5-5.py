def factorial_iterative(n): # 반복문을 사용한 팩토리얼
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def factorial_recursive(n): # 재귀 함수를 사용한 팩토리얼
    if n <= 1:
        return 1
    return n * factorial_iterative(n - 1)

print('반복적으로 구현:', factorial_iterative(5))
print('재귀적으로 구현:', factorial_recursive(5))