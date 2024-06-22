a, b, c = map(int, input().split())
max_num = 0

# 같은 눈이 3개 나왔을 때
if a == b == c :
    print(10000 + (a*1000))
elif a == b or b == c or a == c:
    if a == b :
        print(1000 + (a*100))
    if b == c :
        print(1000 + (b*100))
    if a == c :
        print(1000 + (c*100))
else:
    if a > b and a > c :
        max_num = a
    elif b > a and b > c :
        max_num = b
    else :
        max_num = c

    print(max_num * 100)

# 리스트를 사용하면
