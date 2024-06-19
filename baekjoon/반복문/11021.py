t = int(input())

for i in range(0, t, 1):
    a, b = map(int, input().split())
    print("Case #%d: %d" %(i + 1, a + b))
