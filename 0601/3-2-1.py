# 완성 코드
n, m, k = map(int, input().split())
nlist = list(map(int, input().split()))

nlist.sort()
nlist.reverse()

first = nlist[0]
second = nlist[0+1]

result = 0

while True : # 무한 반복
    for i in range(k): # k번(3번)만큼 반복
        if m == 0 :
            break
        result += first # 제일 큰 수 더하기
        m -= 1 # k번(3번) 다 더하면 두 번째 큰 수를 더해야 하므로
    if m == 0 : # m이 0일 때 while 반복문 탈출
        break
    result += second # m이 0이면 두 번째 큰 수를 더함
    m -= 1

print(result)
