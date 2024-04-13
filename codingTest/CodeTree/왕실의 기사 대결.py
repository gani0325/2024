"""
왕실의 기사 대결

💛 문제
왕실의 기사들은 L×L 크기의 체스판 위에서 대결을 준비하고 있습니다. 체스판의 왼쪽 상단은 (1,1)로 시작하며, 각 칸은 빈칸, 함정, 또는 벽으로 구성되어 있습니다. 
체스판 밖도 벽으로 간주합니다.

왕실의 기사들은 자신의 마력으로 상대방을 밀쳐낼 수 있습니다. 
각 기사의 초기위치는 (r,c)로 주어지며, 그들은 방패를 들고 있기 때문에 (r,c)를 좌측 상단으로 하며 h(높이) × w(너비) 크기의 직사각형 형태를 띄고 있습니다.
각 기사의 체력은 k로 주어집니다.

(1) 기사 이동
왕에게 명령을 받은 기사는 상하좌우 중 하나로 한 칸 이동할 수 있습니다. 이때 만약 이동하려는 위치에 다른 기사가 있다면 그 기사도 함께 연쇄적으로 한 칸 밀려나게 됩니다. 
그 옆에 또 기사가 있다면 연쇄적으로 한 칸씩 밀리게 됩니다. 하지만 만약 기사가 이동하려는 방향의 끝에 벽이 있다면 모든 기사는 이동할 수 없게 됩니다. 
또, 체스판에서 사라진 기사에게 명령을 내리면 아무런 반응이 없게 됩니다.

(2) 대결 대미지
명령을 받은 기사가 다른 기사를 밀치게 되면, 밀려난 기사들은 피해를 입게 됩니다. 
이때 각 기사들은 해당 기사가 이동한 곳에서 w × h 직사각형 내에 놓여 있는 함정의 수만큼만 피해를 입게 됩니다. 
각 기사마다 피해를 받은 만큼 체력이 깎이게 되며, 현재 체력 이상의 대미지를 받을 경우 기사는 체스판에서 사라지게 됩니다. 
단, 명령을 받은 기사는 피해를 입지 않으며, 기사들은 모두 밀린 이후에 대미지를 입게 됩니다. 
밀렸더라도 밀쳐진 위치에 함정이 전혀 없다면 그 기사는 피해를 전혀 입지 않게 됨에 유의합니다.

Q 번에 걸쳐 왕의 명령이 주어졌을 때, Q 번의 대결이 모두 끝난 후 생존한 기사들이 총 받은 대미지의 합을 출력하는 프로그램을 작성해보세요.

🧡 입력 형식
첫 번째 줄에 L, N, Q가 공백을 사이에 두고 주어집니다.
다음 L 개의 줄에 걸쳐서 L×L 크기의 체스판에 대한 정보가 주어집니다.
0이라면 빈칸을 의미합니다.
1이라면 함정을 의미합니다.
2라면 벽을 의미합니다.

다음 N 개의 줄에 걸쳐서 초기 기사들의 정보가 주어집니다. 이 정보는 (r,c,h,w,k) 순으로 주어지며, 
이는 기사의 처음 위치는 (r,c)를 좌측 상단 꼭지점으로 하며 세로 길이가 h, 가로 길이가 w인 직사각형 형태를 띄고 있으며 초기 체력이 k라는 것을 의미합니다. 
입력은 1번 기사부터 N번 기사까지 순서대로 정보가 주어집니다.

단, 처음 주어지는 기사들의 위치는 기사들끼리 서로 겹쳐져 있지 않습니다. 또한 기사와 벽은 겹쳐서 주어지지 않습니다.
다음 Q 개의 줄에 걸쳐 왕의 명령에 대한 정보가 주어집니다. 이 정보는 (i,d) 형태로 주어지며 이는 i번 기사에게 방향 d로 한 칸 이동하라는 명령임을 뜻합니다. 
i는 1 이상 N 이하의 값을 갖으며, 이미 사라진 기사 번호가 주어질 수도 있음에 유의합니다. d는 0, 1, 2, 3 중에 하나이며 각각 위쪽, 오른쪽, 아래쪽, 왼쪽 방향을 의미합니다.

L: 체스판의 크기 (3≤L≤40)
N: 기사의 수 (1≤N≤30)
Q: 명령의 수 (1≤Q≤100)
k: 기사의 체력 (1≤k≤100)

💚 출력 형식
Q 개의 명령이 진행된 이후, 생존한 기사들이 총 받은 대미지의 합을 출력합니다.

⭐ 입출력
입력:
4 3 3
0 0 1 0
0 0 1 0
1 1 0 1
0 0 2 0
1 2 2 1 5
2 1 2 1 1
3 2 1 2 3
1 2
2 1
3 3

출력:
3
"""

from collections import deque

# 전역 변수들을 정의합니다.
MAX_N = 31
MAX_L = 41
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

info = [[0 for _ in range(MAX_L)] for _ in range(MAX_L)]
bef_k = [0 for _ in range(MAX_N)]
r = [0 for _ in range(MAX_N)]
c = [0 for _ in range(MAX_N)]
h = [0 for _ in range(MAX_N)]
w = [0 for _ in range(MAX_N)]
k = [0 for _ in range(MAX_N)]
nr = [0 for _ in range(MAX_N)]
nc = [0 for _ in range(MAX_N)]
dmg = [0 for _ in range(MAX_N)]
is_moved = [False for _ in range(MAX_N)]


# 움직임을 시도해봅니다.
def try_movement(idx, dir):
    q = deque()
    is_pos = True

    # 초기화 작업입니다.
    for i in range(1, n + 1):
        dmg[i] = 0
        is_moved[i] = False
        nr[i] = r[i]
        nc[i] = c[i]

    q.append(idx)
    is_moved[idx] = True

    while q:
        x = q.popleft()

        nr[x] += dx[dir]
        nc[x] += dy[dir]

        # 경계를 벗어나는지 체크합니다.
        if nr[x] < 1 or nc[x] < 1 or nr[x] + h[x] - 1 > l or nc[x] + w[x] - 1 > l:
            return False

        # 대상 조각이 다른 조각이나 장애물과 충돌하는지 검사합니다.
        for i in range(nr[x], nr[x] + h[x]):
            for j in range(nc[x], nc[x] + w[x]):
                if info[i][j] == 1:
                    dmg[x] += 1
                if info[i][j] == 2:
                    return False

        # 다른 조각과 충돌하는 경우, 해당 조각도 같이 이동합니다.
        for i in range(1, n + 1):
            if is_moved[i] or k[i] <= 0:
                continue
            if r[i] > nr[x] + h[x] - 1 or nr[x] > r[i] + h[i] - 1:
                continue
            if c[i] > nc[x] + w[x] - 1 or nc[x] > c[i] + w[i] - 1:
                continue

            is_moved[i] = True
            q.append(i)

    dmg[idx] = 0
    return True


# 특정 조각을 지정된 방향으로 이동시키는 함수입니다.
def move_piece(idx, move_dir):
    if k[idx] <= 0:
        return

    # 이동이 가능한 경우, 실제 위치와 체력을 업데이트합니다.
    if try_movement(idx, move_dir):
        # 기사의 처음 위치는 (r,c)를 좌측 상단 꼭지점으로 하며 세로 길이가 h, 가로 길이가 w인 직사각형 형태를 띄고 있으며 초기 체력이 k라는 것
        for i in range(1, n + 1):
            r[i] = nr[i]
            c[i] = nc[i]
            k[i] -= dmg[i]


# 입력값을 받습니다.
l, n, q = map(int, input().split())
for i in range(1, l + 1):
    info[i][1:] = map(int, input().split())
for i in range(1, n + 1):
    r[i], c[i], h[i], w[i], k[i] = map(int, input().split())
    bef_k[i] = k[i]

for _ in range(q):
    idx, d = map(int, input().split())
    move_piece(idx, d)

# 결과를 계산하고 출력합니다.
ans = sum([bef_k[i] - k[i] for i in range(1, n + 1) if k[i] > 0])
print(ans)