
# while True:
#     a, b = map(int, input().split())
#     print(a + b)
#
#     if EOFError:
#         break

while True:
    try:
        A, B = map(int, input().split())
        print(A+B)
    except EOFError:
        break
