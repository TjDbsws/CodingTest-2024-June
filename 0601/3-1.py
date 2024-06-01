# 완성 코드
n = 1260
count = 0
coins = [500, 100, 50, 10] # 화폐를 리스트로 생성하여 반복문 이용

for coin in coins:
    count += n // coin # 해당 화폐로 거슬러 줄 수 있는 동전의 개수
    n %= coin # n을 리스트 안의 요소로 나눈 나머지로 반복해서 변경

print("count =", count)
