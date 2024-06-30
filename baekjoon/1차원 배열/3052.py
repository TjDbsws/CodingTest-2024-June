datas = []

for _ in range(10):
    n = int(input())
    data = n % 42
    if data not in datas:
        datas.append(data)

print(len(datas))
