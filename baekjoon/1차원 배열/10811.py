n, m = map(int, input().split())
data = [i for i in range(1, n+1)]

for _ in range(m):
    i, j = map(int, input().split())

    change = data[i-1:j]
    change.reverse()
    data[i-1:j] = change

print(*data)
