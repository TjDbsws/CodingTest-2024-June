# 단순하게 풀기

a = int(input())
b = input()

print(a*int(b[2]))
print(a*int(b[1]))
print(a*int(b[0]))
print(a*int(b))

# 반복문 사용하기

a = int(input())
b = input()

for i in range(3, 0, -1): # for문 사용 시 주의
    print(a*int(b[i-1]))
print(a*int(b))
