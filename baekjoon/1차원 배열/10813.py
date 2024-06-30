n, m = map(int, input().split())
data = [i for i in range(1, n+1)]
change = 0

for _ in range(m):
    i, j = map(int, input().split())
    change = data[i-1]
    data[i-1] = data[j-1]
    data[j-1] = change

print(*data)
