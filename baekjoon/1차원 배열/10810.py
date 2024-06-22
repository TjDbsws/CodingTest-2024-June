n, m = map(int, input().split())
arr = [0 for _ in range(n)]

for _ in range(m):
    i, j, k = map(int, input().split())
    for x in range(i-1, j):
        arr[x] = k

for y in range(n):
    print(arr[y], end=' ')
