# 맵 크기 저장
n, m = map(int, input().split())
# 현재 위치와 방향 입력 받기
x, y, direction = map(int, input().split())
# 지형 상태 입력 받기
array = []
for i in range(n):
    array.append(list(map(int, input().split())))
# 가본 칸 저장하기
d = [[0] * m for _ in range(n)]
d[x][y] = 1
# 방문한 칸의 수 저장
count = 0

# 이동할 곳 확인용?
nx, ny = 0, 0

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전하는 함수 정의
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

count = 1

# 네 방향 모두 갈 수 없을 때 확인용
turn_time = 0

while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 회전한 이후 정면에 가보지 않은 칸이 있을 경우
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1 # 가본 곳에 추가
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    # 회전한 이후 정면에 가본 칸이거나 바다인 경우
    else:
        turn_time += 1 # 회전하기
    # 회전하였음에도 네 방향 다 갈 수 없을 때
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 갈 수 있을 경우
        if array[nx][ny] == 0:
            x = nx
            y = ny
        # 뒤가 막힌 경우
        else:
            break
        turn_time = 0

print(count)
