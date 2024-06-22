n = int(input())
arr = list(map(int, input().split()))
first = arr[0]
last = arr[0]

for i in range(n):
    if first < arr[i]:
        first = arr[i]
    if last > arr[i]:
        last = arr[i]

print(last, first)