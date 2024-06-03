h, m = map(int, input().split())
add_m = int(input())

m += add_m

if m >= 60: # m = 85
    m -= 60
    h += 1

if h >= 24: # m = 26
    h -= 24

print(h, m)
