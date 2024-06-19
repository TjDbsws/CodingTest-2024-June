n = int(input()) # 공간의 크기 저장
x, y = 1, 1 # 현재 위치
plans = input().split() # 이동 계획 저장

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

nx, ny = 0, 0

for plan in plans: # 이동 계획을 하나씩 반복
    for i in range(len(move_types)): # 'L', 'R', 'U', 'D'만큼 반복
        if plan == move_types[i]: # 이동 계획이랑 같은 계획을 리스트에서 찾음
            nx = x + dx[i]
            ny = y + dy[i]
        if nx < 1 or ny < 1 or nx > n or ny > n:
            continue
        x, y = nx, ny

print(x, y)


