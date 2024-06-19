import sys

t = int(input())

while t > 0:
    a, b = map(int, sys.stdin.readline().split())
    t -= 1
    print(a + b)
