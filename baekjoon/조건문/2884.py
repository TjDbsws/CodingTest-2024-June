# 0 <= h <= 23, 0 <= m <= 59

h, m = map(int, input().split())

if m >= 45:
    print(h, m-45)
else:
    m += 60
    m -= 45
    h -= 1
    if h < 0: # h == 0은 안 됨. 위에서 h = -1일 땐 실행이 안 되기 때문
        h = 23

print(h, m)


