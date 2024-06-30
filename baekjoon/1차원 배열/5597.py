data = [i for i in range(1, 31)]
printArr = [0]

for i in range(28):
    num = int(input())
    if num in data:
        printArr.append(num)

for d in range(1, 31):
    if d not in printArr:
        print(d)
