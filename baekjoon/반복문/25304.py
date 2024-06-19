total_price = int(input())
total_n = int(input())
total = 0

while total_n > 0:
    price, n = map(int, input().split())
    total += price * n
    total_n -= 1

if total == total_price:
    print("Yes")
else:
    print("No")
