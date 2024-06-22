h, m = map(int, input().split())
add_m = int(input())

total_min = h * 60 + m + add_m

h = (total_min // 60) % 24
m = total_min % 60

print(h, m)
