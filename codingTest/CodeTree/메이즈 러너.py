"""
메이즈 러너

💛 문제
M명의 참가자가 미로 탈출하기 게임에 참가하였습니다.
미로의 구성은 다음과 같습니다.
    미로는 N×N 크기의 격자입니다. 각 위치는 (r,c)의 형태로 표현되며, 아래로 갈수록 r이 증가, 오른쪽으로 갈수록 c가 증가합니다. 좌상단은 (1,1)입니다.
    미로의 각 칸은 다음 3가지 중 하나의 상태를 갖습니다.
    빈 칸 : 참가자가 이동 가능한 칸입니다.
    벽 : 참가자가 이동할 수 없는 칸입니다.
    1이상 9이하의 내구도를 갖고 있습니다.
    회전할 때, 내구도가 1씩 깎입니다.
    내구도가 0이 되면, 빈 칸으로 변경됩니다.
    출구 : 참가자가 해당 칸에 도달하면, 즉시 탈출합니다.

1초마다 모든 참가자는 한 칸씩 움직입니다. 움직이는 조건은 다음과 같습니다.
    두 위치 (x1,y1), (x2,y2)의 최단거리는 ∣x1−x2∣+∣y1−y2∣로 정의됩니다.
    모든 참가자는 동시에 움직입니다.
    상하좌우로 움직일 수 있으며, 벽이 없는 곳으로 이동할 수 있습니다.
    움직인 칸은 현재 머물러 있던 칸보다 출구까지의 최단 거리가 가까워야 합니다.
    움직일 수 있는 칸이 2개 이상이라면, 상하로 움직이는 것을 우선시합니다.
    참가가가 움직일 수 없는 상황이라면, 움직이지 않습니다.
    한 칸에 2명 이상의 참가자가 있을 수 있습니다.
    모든 참가자가 이동을 끝냈으면, 다음 조건에 의해 미로가 회전합니다.

한 명 이상의 참가자와 출구를 포함한 가장 작은 정사각형을 잡습니다.
가장 작은 크기를 갖는 정사각형이 2개 이상이라면, 좌상단 r 좌표가 작은 것이 우선되고, 그래도 같으면 c 좌표가 작은 것이 우선됩니다.
선택된 정사각형은 시계방향으로 90도 회전하며, 회전된 벽은 내구도가 1씩 깎입니다.
K초 동안 위의 과정을 계속 반복됩니다. 만약 K초 전에 모든 참가자가 탈출에 성공한다면, 게임이 끝납니다. 
게임이 끝났을 때, 모든 참가자들의 이동 거리 합과 출구 좌표를 출력하는 프로그램을 작성해보세요.

🧡 입력 형식
첫 번째 줄에 N, M, K가 공백을 사이에 두고 주어집니다.
다음 N개의 줄에 걸쳐서 N×N 크기의 미로에 대한 정보가 주어집니다.

0이라면, 빈 칸을 의미합니다.
1이상 9이하의 값을 갖는다면, 벽을 의미하며, 해당 값은 내구도를 뜻합니다.
다음 M개의 줄에 걸쳐서 참가자의 좌표가 주어집니다. 모든 참가자는 초기에 빈 칸에만 존재합니다.

다음 줄에 출구의 좌표가 주어집니다. 출구는 빈 칸에만 주어집니다.
N: 미로의 크기 (4≤N≤10)
M: 참가자 수 (1≤M≤10)
K: 게임 시간 (1≤K≤100)

💚 출력 형식
게임 시작 후 K초가 지났거나, 모든 참가자가 미로를 탈출했을 때, 모든 참가자들의 이동 거리 합과 출구 좌표를 출력합니다.

⭐ 입출력
입력:
5 3 8
0 0 0 0 1
9 2 2 0 0
0 1 0 1 0
0 0 0 1 0
0 0 0 0 0
1 3
3 1
3 5
3 3

출력:
7
1 1
"""

n, m, k = tuple(map(int, input().split()))
# 모든 벽들의 상태를 기록해줍니다.
board = [
    [0] * (n + 1)
    for _ in range(n + 1)
]

for i in range(1, n + 1):
    board[i] = [0] + list(map(int, input().split()))

# 회전의 구현을 편하게 하기 위해 2차원 배열을 하나 더 정의해줍니다.
next_board = [
    [0] * (n + 1)
    for _ in range(n + 1)
]

# 참가자의 위치 정보를 기록해줍니다.
traveler = [(-1, -1)] + [
    tuple(map(int, input().split()))
    for _ in range(m)
]

# 출구의 위치 정보를 기록해줍니다.
exits = tuple(map(int, input().split()))

# 정답(모든 참가자들의 이동 거리 합)을 기록해줍니다.
ans = 0

# 회전해야 하는 최소 정사각형을 찾아 기록해줍니다.
sx, sy, square_size = 0, 0, 0


# 모든 참가자를 이동시킵니다.
def move_all_traveler():
    global exits, ans

    # m명의 모든 참가자들에 대해 이동을 진행합니다.
    for i in range(1, m + 1):
        # 이미 출구에 있는 경우 스킵합니다.
        if traveler[i] == exits:
            continue
        
        tx, ty = traveler[i]
        ex, ey = exits

        # 행이 다른 경우 행을 이동시켜봅니다.
        if tx != ex:
            nx, ny = tx, ty

            if ex > nx: 
                nx += 1
            else:
                nx -= 1

            # 벽이 없다면 행을 이동시킬 수 있습니다.
            # 이 경우 행을 이동시키고 바로 다음 참가자로 넘어갑니다.
            if not board[nx][ny]:
                traveler[i] = (nx, ny)
                ans += 1
                continue

        # 열이 다른 경우 열을 이동시켜봅니다.
        if ty != ey:
            nx, ny = tx, ty

            if ey > ny: 
                ny += 1
            else:
                ny -= 1

            # 벽이 없다면 행을 이동시킬 수 있습니다.
            # 이 경우 열을 이동시킵니다.
            if not board[nx][ny]:
                traveler[i] = (nx, ny)
                ans += 1
                continue


# 한 명 이상의 참가자와 출구를 포함한 가장 작은 정사각형을 찾습니다.
def find_minimum_square():
    global exits, sx, sy, square_size
    ex, ey = exits

    # 가장 작은 정사각형부터 모든 정사각형을 만들어봅니다.
    for sz in range(2, n + 1):
        # 가장 좌상단 r 좌표가 작은 것부터 하나씩 만들어봅니다.
        for x1 in range(1, n - sz + 2):
            # 가장 좌상단 c 좌표가 작은 것부터 하나씩 만들어봅니다.
            for y1 in range(1, n - sz + 2):
                x2, y2 = x1 + sz - 1, y1 + sz - 1

                # 만약 출구가 해당 정사각형 안에 없다면 스킵합니다.
                if not (x1 <= ex and ex <= x2 and y1 <= ey and ey <= y2):
                    continue

                # 한 명 이상의 참가자가 해당 정사각형 안에 있는지 판단합니다.
                is_traveler_in = False
                for l in range(1, m + 1):
                    tx, ty = traveler[l]
                    if x1 <= tx and tx <= x2 and y1 <= ty and ty <= y2:
                        # 출구에 있는 참가자는 제외합니다.
                        if not (tx == ex and ty == ey):
                            is_traveler_in = True

                # 만약 한 명 이상의 참가자가 해당 정사각형 안에 있다면
                # sx, sy, square_size 정보를 갱신하고 종료합니다.
                if is_traveler_in:
                    sx = x1
                    sy = y1
                    square_size = sz

                    return


# 정사각형 내부의 벽을 회전시킵니다.
def rotate_square():
    # 우선 정사각형 안에 있는 벽들을 1 감소시킵니다.
    for x in range(sx, sx + square_size):
        for y in range(sy, sy + square_size):
            if board[x][y]: 
                board[x][y] -= 1

    # 정사각형을 시계방향으로 90' 회전합니다.
    for x in range(sx, sx + square_size):
        for y in range(sy, sy + square_size):
            # Step 1. (sx, sy)를 (0, 0)으로 옮겨주는 변환을 진행합니다. 
            ox, oy = x - sx, y - sy
            # Step 2. 변환된 상태에서는 회전 이후의 좌표가 (x, y) . (y, square_n - x - 1)가 됩니다.
            rx, ry = oy, square_size - ox - 1
            # Step 3. 다시 (sx, sy)를 더해줍니다.
            next_board[rx + sx][ry + sy] = board[x][y]

    # next_board 값을 현재 board에 옮겨줍니다.
    for x in range(sx, sx + square_size):
        for y in range(sy, sy + square_size):
            board[x][y] = next_board[x][y]


# 모든 참가자들 및 출구를 회전시킵니다.
def rotate_traveler_and_exit():
    global exits

    # m명의 참가자들을 모두 확인합니다.
    for i in range(1, m + 1):
        tx, ty = traveler[i]
        # 해당 참가자가 정사각형 안에 포함되어 있을 때에만 회전시킵니다.
        if sx <= tx and tx < sx + square_size and sy <= ty and ty < sy + square_size:
            # Step 1. (sx, sy)를 (0, 0)으로 옮겨주는 변환을 진행합니다. 
            ox, oy = tx - sx, ty - sy
            # Step 2. 변환된 상태에서는 회전 이후의 좌표가 (x, y) . (y, square_n - x - 1)가 됩니다.
            rx, ry = oy, square_size - ox - 1
            # Step 3. 다시 (sx, sy)를 더해줍니다.
            traveler[i] = (rx + sx, ry + sy)

    # 출구에도 회전을 진행합니다.
    ex, ey = exits
    if sx <= ex and ex < sx + square_size and sy <= ey and ey < sy + square_size:
        # Step 1. (sx, sy)를 (0, 0)으로 옮겨주는 변환을 진행합니다. 
        ox, oy = ex - sx, ey - sy
        # Step 2. 변환된 상태에서는 회전 이후의 좌표가 (x, y) . (y, square_n - x - 1)가 됩니다.
        rx, ry = oy, square_size - ox - 1
        # Step 3. 다시 (sx, sy)를 더해줍니다.
        exits = (rx + sx, ry + sy)


for _ in range(k):
    # 모든 참가자를 이동시킵니다.
    move_all_traveler()

    # 모든 사람이 출구로 탈출했는지 판단합니다.
    is_all_escaped = True
    for i in range(1, m + 1):
        if traveler[i] != exits:
            is_all_escaped = False

    # 만약 모든 사람이 출구로 탈출했으면 바로 종료합니다.
    if is_all_escaped: 
        break

    # 한 명 이상의 참가자와 출구를 포함한 가장 작은 정사각형을 찾습니다.
    find_minimum_square()

    # 정사각형 내부의 벽을 회전시킵니다.
    rotate_square()
    # 모든 참가자들 및 출구를 회전시킵니다.
    rotate_traveler_and_exit()

print(ans)

ex, ey = exits
print(ex, ey)