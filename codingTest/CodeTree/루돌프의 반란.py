"""
루돌프의 반란

💛 문제
1번부터 P번까지 P 명의 산타들이 크리스마스 이브를 준비하던 중, 산타의 주요 수송수단인 루돌프가 반란을 일으켰습니다. 
루돌프는 산타들을 박치기하여 산타의 선물 배달을 방해하려고 합니다. 산타들은 루돌프를 잡아서 크리스마스를 구해야 합니다!

(1) 게임판의 구성
게임판은 N×N 크기의 격자로 이루어져 있습니다. 각 위치는 (r,c)의 형태로 표현되며, 아래로 갈수록 r이 증가, 오른쪽으로 갈수록 c가 증가합니다. 좌상단은 (1,1)입니다.
게임은 총 M 개의 턴에 걸쳐 진행되며 매 턴마다 루돌프와 산타들이 한 번씩 움직입니다. 루돌프가 한 번 움직인 뒤, 1번 산타부터 P번 산타까지 순서대로 움직이게 됩니다. 
이때 기절해있거나 격자 밖으로 빠져나가 게임에서 탈락한 산타들은 움직일 수 없습니다.
게임판에서 두 칸 (r 1 ,c 1​ ), (r 2​ ,c 2​ ) 사이의 거리는 (r 1​ −r 2​ ) 2 +(c 1​ −c 2​ ) 2 으로 계산됩니다.

(2) 루돌프의 움직임
루돌프는 가장 가까운 산타를 향해 1칸 돌진합니다. 단, 게임에서 탈락하지 않은 산타 중 가장 가까운 산타를 선택해야 합니다.
만약 가장 가까운 산타가 2명 이상이라면, r 좌표가 큰 산타를 향해 돌진합니다. r이 동일한 경우, c 좌표가 큰 산타를 향해 돌진합니다.
루돌프는 상하좌우, 대각선을 포함한 인접한 8방향 중 하나로 돌진할 수 있습니다. 
(편의상 인접한 대각선 방향으로 전진하는 것도 1칸 전진하는 것이라 생각합니다.) 가장 우선순위가 높은 산타를 향해 8방향 중 가장 가까워지는 방향으로 한 칸 돌진합니다.

(3) 산타의 움직임
산타는 1번부터 P번까지 순서대로 움직입니다.
기절했거나 이미 게임에서 탈락한 산타는 움직일 수 없습니다.
산타는 루돌프에게 거리가 가장 가까워지는 방향으로 1칸 이동합니다.
산타는 다른 산타가 있는 칸이나 게임판 밖으로는 움직일 수 없습니다.
움직일 수 있는 칸이 없다면 산타는 움직이지 않습니다.
움직일 수 있는 칸이 있더라도 만약 루돌프로부터 가까워질 수 있는 방법이 없다면 산타는 움직이지 않습니다.
산타는 상하좌우로 인접한 4방향 중 한 곳으로 움직일 수 있습니다. 이때 가장 가까워질 수 있는 방향이 여러 개라면, 상우하좌 우선순위에 맞춰 움직입니다.

(4) 충돌
산타와 루돌프가 같은 칸에 있게 되면 충돌이 발생합니다.
루돌프가 움직여서 충돌이 일어난 경우, 해당 산타는 C만큼의 점수를 얻게 됩니다. 이와 동시에 산타는 루돌프가 이동해온 방향으로 C 칸 만큼 밀려나게 됩니다.
산타가 움직여서 충돌이 일어난 경우, 해당 산타는 D만큼의 점수를 얻게 됩니다. 이와 동시에 산타는 자신이 이동해온 반대 방향으로 D 칸 만큼 밀려나게 됩니다.
밀려나는 것은 포물선 모양을 그리며 밀려나는 것이기 때문에 이동하는 도중에 충돌이 일어나지는 않고 정확히 원하는 위치에 도달하게 됩니다.
만약 밀려난 위치가 게임판 밖이라면 산타는 게임에서 탈락됩니다.
만약 밀려난 칸에 다른 산타가 있는 경우 상호작용이 발생합니다.

(5) 상호작용
루돌프와의 충돌 후 산타는 포물선의 궤적으로 이동하여 착지하게 되는 칸에서만 상호작용이 발생할 수 있습니다.
산타는 충돌 후 착지하게 되는 칸에 다른 산타가 있다면 그 산타는 1칸 해당 방향으로 밀려나게 됩니다. 그 옆에 산타가 있다면 연쇄적으로 1칸씩 밀려나는 것을 반복하게 됩니다. 
게임판 밖으로 밀려나오게 된 산타의 경우 게임에서 탈락됩니다.

(6) 기절
산타는 루돌프와의 충돌 후 기절을 하게 됩니다. 현재가 k번째 턴이었다면, (k+1)번째 턴까지 기절하게 되어 (k+2)번째 턴부터 다시 정상상태가 됩니다.
기절한 산타는 움직일 수 없게 됩니다. 단, 기절한 도중 충돌이나 상호작용으로 인해 밀려날 수는 있습니다.
루돌프는 기절한 산타를 돌진 대상으로 선택할 수 있습니다.

(7) 게임 종료
M 번의 턴에 걸쳐 루돌프, 산타가 순서대로 움직인 이후 게임이 종료됩니다.
만약 P 명의 산타가 모두 게임에서 탈락하게 된다면 그 즉시 게임이 종료됩니다.
매 턴 이후 아직 탈락하지 않은 산타들에게는 1점씩을 추가로 부여합니다.
게임이 끝났을 때 각 산타가 얻은 최종 점수를 구하는 프로그램을 작성해보세요.

🧡 입력 형식
첫 번째 줄에 N, M, P, C, D가 공백을 사이에 두고 주어집니다.

다음 줄에는 루돌프의 초기 위치 (R r​ ,R c​ ) 가 주어집니다.
다음 P 개의 줄에 걸쳐서 산타의 번호 P n​ 과 초기 위치 (S r​ ,S c​ )가 공백을 사이에 두고 주어집니다.

처음 산타와 루돌프의 위치는 겹쳐져 주어지지 않음을 가정해도 좋습니다.

N: 게임판의 크기 (3≤N≤50)
M: 게임 턴 수 (1≤M≤1000)
P: 산타의 수 (1≤P≤30)
C: 루돌프의 힘 (1≤C≤N)
D: 산타의 힘 (1≤D≤N)
P n​ : 산타의 번호 (1≤P n​ ≤P)
(R r​ ,R c​ ): 루돌프의 초기 위치 (1≤R r​ ,R c​ ≤N)
(S r​ ,S c​ ): 산타의 초기 위치 (1≤S r​ ,S c​ ≤N)

💚 출력 형식
게임이 끝났을 때 각 산타가 얻은 최종 점수를 1번부터 P번까지 순서대로 공백을 사이에 두고 출력합니다.

⭐ 입출력
입력:
5 7 4 2 2
3 2
1 1 3
2 3 5
3 5 1
4 4 4

출력:
11 6 2 7
"""

# (x, y)가 보드 내의 좌표인지 확인하는 함수입니다.
def is_inrange(x, y):
    return 1 <= x and x <= n and 1 <= y and y <= n

n, m, p, c, d = map(int, input().split())
rudolf = tuple(map(int, input().split()))

points = [0 for _ in range(p + 1)]
pos = [(0, 0) for _ in range(p + 1)]
board = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
is_live = [False for _ in range(p + 1)]
stun = [0 for _ in range(p + 1)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

board[rudolf[0]][rudolf[1]] = -1

for _ in range(p):
    id, x, y = tuple(map(int, input().split()))
    pos[id] = (x, y)
    board[pos[id][0]][pos[id][1]] = id
    is_live[id] = True

for t in range(1, m + 1):
    closestX, closestY, closestIdx = 10000, 10000, 0

    # 살아있는 포인트 중 루돌프에 가장 가까운 산타를 찾습니다.
    for i in range(1, p + 1):
        if not is_live[i]:
            continue

        currentBest = ((closestX - rudolf[0]) ** 2 + (closestY - rudolf[1]) ** 2, (-closestX, -closestY))
        currentValue = ((pos[i][0] - rudolf[0]) ** 2 + (pos[i][1] - rudolf[1]) ** 2, (-pos[i][0], -pos[i][1]))

        if currentValue < currentBest:
            closestX, closestY = pos[i]
            closestIdx = i

    # 가장 가까운 산타의 방향으로 루돌프가 이동합니다.
    if closestIdx:
        prevRudolf = rudolf
        moveX = 0
        if closestX > rudolf[0]:
            moveX = 1
        elif closestX < rudolf[0]:
            moveX = -1

        moveY = 0
        if closestY > rudolf[1]:
            moveY = 1
        elif closestY < rudolf[1]:
            moveY = -1

        rudolf = (rudolf[0] + moveX, rudolf[1] + moveY)
        board[prevRudolf[0]][prevRudolf[1]] = 0

    # 루돌프의 이동으로 충돌한 경우, 산타를 이동시키고 처리를 합니다.
    if rudolf[0] == closestX and rudolf[1] == closestY:
        firstX = closestX + moveX * c
        firstY = closestY + moveY * c
        lastX, lastY = firstX, firstY

        stun[closestIdx] = t + 1

        # 만약 이동한 위치에 산타가 있을 경우, 연쇄적으로 이동이 일어납니다.
        while is_inrange(lastX, lastY) and board[lastX][lastY] > 0:
            lastX += moveX
            lastY += moveY

        # 연쇄적으로 충돌이 일어난 가장 마지막 위치에서 시작해,
        # 순차적으로 보드판에 있는 산타를 한칸씩 이동시킵니다.
        while not (lastX == firstX and lastY == firstY):
            beforeX = lastX - moveX
            beforeY = lastY - moveY

            if not is_inrange(beforeX, beforeY):
                break

            idx = board[beforeX][beforeY]

            if not is_inrange(lastX, lastY):
                is_live[idx] = False
            else:
                board[lastX][lastY] = board[beforeX][beforeY]
                pos[idx] = (lastX, lastY)

            lastX, lastY = beforeX, beforeY

        points[closestIdx] += c
        pos[closestIdx] = (firstX, firstY)
        if is_inrange(firstX, firstY):
            board[firstX][firstY] = closestIdx
        else:
            is_live[closestIdx] = False

    board[rudolf[0]][rudolf[1]] = -1;

    # 각 산타들은 루돌프와 가장 가까운 방향으로 한칸 이동합니다.
    for i in range(1, p+1):
        if not is_live[i] or stun[i] >= t:
            continue

        minDist = (pos[i][0] - rudolf[0])**2 + (pos[i][1] - rudolf[1])**2
        moveDir = -1

        for dir in range(4):
            nx = pos[i][0] + dx[dir]
            ny = pos[i][1] + dy[dir]

            if not is_inrange(nx, ny) or board[nx][ny] > 0:
                continue

            dist = (nx - rudolf[0])**2 + (ny - rudolf[1])**2
            if dist < minDist:
                minDist = dist
                moveDir = dir

        if moveDir != -1:
            nx = pos[i][0] + dx[moveDir]
            ny = pos[i][1] + dy[moveDir]

            # 산타의 이동으로 충돌한 경우, 산타를 이동시키고 처리를 합니다.
            if nx == rudolf[0] and ny == rudolf[1]:
                stun[i] = t + 1

                moveX = -dx[moveDir]
                moveY = -dy[moveDir]

                firstX = nx + moveX * d
                firstY = ny + moveY * d
                lastX, lastY = firstX, firstY

                if d == 1:
                    points[i] += d
                else:
                    # 만약 이동한 위치에 산타가 있을 경우, 연쇄적으로 이동이 일어납니다.
                    while is_inrange(lastX, lastY) and board[lastX][lastY] > 0:
                        lastX += moveX
                        lastY += moveY

                    # 연쇄적으로 충돌이 일어난 가장 마지막 위치에서 시작해,
                    # 순차적으로 보드판에 있는 산타를 한칸씩 이동시킵니다.
                    while lastX != firstX or lastY != firstY:
                        beforeX = lastX - moveX
                        beforeY = lastY - moveY

                        if not is_inrange(beforeX, beforeY):
                            break

                        idx = board[beforeX][beforeY]

                        if not is_inrange(lastX, lastY):
                            is_live[idx] = False
                        else:
                            board[lastX][lastY] = board[beforeX][beforeY]
                            pos[idx] = (lastX, lastY)

                        lastX, lastY = beforeX, beforeY

                    points[i] += d
                    board[pos[i][0]][pos[i][1]] = 0
                    pos[i] = (firstX, firstY)
                    if is_inrange(firstX, firstY):
                        board[firstX][firstY] = i
                    else:
                        is_live[i] = False
            else:
                board[pos[i][0]][pos[i][1]] = 0
                pos[i] = (nx, ny)
                board[nx][ny] = i

    # 라운드가 끝나고 탈락하지 않은 산타들의 점수를 1 증가시킵니다.
    for i in range(1, p+1):
        if is_live[i]:
            points[i] += 1


# 결과를 출력합니다.
for i in range(1, p + 1):
    print(points[i], end=" ")