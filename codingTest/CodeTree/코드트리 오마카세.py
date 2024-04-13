"""
코드트리 오마카세

💛 문제
코드트리 회사에서는 회전 초밥집을 새로 오픈하였습니다. 
고객을 사랑하는 마음에서 시작된 초밥집이기 때문에 주방장이 직접 각 초밥에 사람 이름을 적어서 회전하는 벨트 위에 올려놓는 초밥 오마카세 집입니다.
코드트리 오마카세에는 아래와 같이 원형 형태의 초밥 벨트와 L개의 의자가 놓여있습니다. 의자는 원형에서 x=0을 기점으로 시계방향으로 돌며 
x=1,...,x=L−1 위치까지 총 L개가 등간격으로 놓여있습니다. 회전 초밥은 각 의자 앞에 여러 개 놓일 수 있으며 초밥 벨트는 1초에 한 칸씩 시계방향으로 회전합니다. 
처음에는 벨트 위에 놓여 있는 초밥이 전혀 없으며 의자 위에 앉아 있는 사람 역시 없습니다.

코드트리 오마카세는 3가지 명령에 따라 진행됩니다.
(1) 주방장의 초밥 만들기
주방장은 시각 t에 위치 x 앞에 있는 벨트 위에 name 이름을 부착한 회전 초밥을 하나 올려놓습니다. 
단, 이 과정은 시각 t에 초밥 회전이 일어난 직후에 발생합니다. 
또, 같은 위치에 여러 회전 초밥이 올라갈 수 있으며 자신의 이름이 적혀 있는 초밥이 같은 위치에 여러 개 놓여 있는 것 역시 가능함에 유의합니다.

(2) 손님 입장
이름이 name인 사람이 시각 t에 위치 x에 있는 의자로 가서 앉습니다. 
단, 이 과정은 시각 t에 초밥 회전이 일어난 직후에 발생합니다. 
이때부터 위치 x 앞으로 오는 초밥들 중 자신의 이름이 적혀있는 초밥을 정확히 n개를 먹고 자리를 떠납니다. 
이 명령이 주어졌을 때 해당 위치에는 사람이 없음을 가정해도 좋습니다. 
만약 시각 t에 위치 x에 자신의 이름이 적혀있는 초밥이 놓여 있다면 자리에 착석하는 즉시 먹게 되며, 
자신의 이름이 적혀 있는 초밥이 같은 위치에 여러 개 있다면 동시에 여러 개를 먹을 수 있습니다. 
또한 초밥을 먹는데에는 시간이 소요되지 않는다고 가정해도 좋습니다.

(3) 사진 촬영
시각 t에 코드트리 오마카세 집의 모습을 촬영합니다. 
이때 시각 t에는 먼저 (1) 초밥 회전이 일어난 뒤 (2) 손님이 자신이 앉아 있는 자리에서 자신의 이름이 적힌 초밥을 먹은 뒤 (3) 사진 촬영을 진행해야 함에 유의합니다.
사진 촬영을 진행했을 때 현재 코드트리 오마카세 집에 있는 사람 수와 남아 있는 초밥 수를 출력하면 됩니다.

Q 번에 걸쳐 명령을 순서대로 진행하며 알맞은 답을 출력하는 프로그램을 작성해보세요.

🧡 입력 형식
첫 번째 줄에 초밥 벨트의 길이 L과 명령의 수 Q가 공백을 사이에 두고 주어집니다.
두 번째 줄부터는 Q개의 줄에 걸쳐 명령의 정보가 주어집니다. 각 명령에 따른 형태는 다음과 같습니다.
주방장의 초밥 만들기
100 t x name 형태로 공백을 사이에 두고 주어집니다. 이는 주방장이 시각 t에 위치 x 앞에 있는 벨트 위에 name 이름을 부착한 회전 초밥을 하나 올려 놓는다는 것을 의미합니다.
손님 입장
200 t x name n 형태로 공백을 사이에 두고 주어집니다. 이는 이름이 name인 사람이 시각 t에 위치 x에 있는 의자로 가서 앉은 뒤 n개의 초밥을 먹을 때까지 기다리게 됨을 의미합니다.
n개의 초밥을 먹게된 직후 자리를 떠나게 됩니다.
오는 손님의 이름은 전부 다르며, 동일한 손님이 다시 방문하게 되는 경우는 없음을 가정해도 좋습니다.
사진 촬영
300 t 형태로 주어집니다. 이 경우 시각 t에 코드트리 오마카세 집에 있는 사람 수와 남아 있는 초밥의 수를 공백을 사이에 두고 출력합니다.
이 명령은 최소 1번 이상 주어진다고 가정해도 좋습니다.
3 ≤ L ≤ 1,000,000,000
1 ≤ Q ≤ 100,000
1 ≤ t ≤ 1,000,000,000
0 ≤ x ≤ L−1
1 ≤ name 의 길이 ≤ 30
1 ≤ 주어지는 서로 다른 name의 수 ≤ 15,000
name 은 소문자 알파벳으로만 이루어져 있습니다.
입력으로 주어지는 t 값은 모두 다르며, 오름차순으로 정렬되어 주어집니다.

또, 시간이 무한히 흘렀을 때 만들어진 모든 초밥은 손님에 의해 다 사라지며, 손님 역시 정확히 n개의 초밥을 먹고 코드트리 오마카세를 떠나게 됨을 가정해도 좋습니다.

💚 출력 형식
300 명령어에 대해 시각 t에 코드트리 오마카세 집에 있는 사람 수와 남아 있는 초밥의 수를 공백을 사이에 두고 한 줄에 하나씩 순서대로 출력합니다.

⭐ 입출력
입력:
5 10
100 1 1 sam
100 2 2 teddy
100 3 2 june
300 6
200 7 4 june 2
200 8 3 teddy 1
300 9
200 10 3 sam 1
100 11 4 june
300 13

출력:
0 3
1 2
0 0
"""

# 변수 선언
L, Q = 0, 0

class Query:
    def __init__(self, cmd, t, x, name, n):
        self.cmd = cmd
        self.t = t
        self.x = x
        self.name = name
        self.n = n

# 명령들을 관리합니다.
queries = []

# 등장한 사람 목록을 관리합니다.
names = set()

# 각 사람마다 주어진 초밥 명령만을 관리합니다.
p_queries = {}

# 각 사람마다 입장 시간을 관리합니다.
entry_time = {}

# 각 손님의 위치를 관리합니다.
position = {}

# 각 사람마다 퇴장 시간을 관리합니다.
exit_time = {}

# Query를 (t, cmd) 순으로 정렬합니다.
def cmp(q1, q2):
    if q1.t != q2.t:
        return q1.t < q2.t
    return q1.cmd < q2.cmd

# 입력:
L, Q = map(int, input().split())

for _ in range(Q):
    command = input().split()
    cmd, t, x, n = -1, -1, -1, -1
    name = ""
    cmd = int(command[0])
    if cmd == 100:
        t, x, name = command[1:]
        t, x = map(int, [t, x])
    elif cmd == 200:
        t, x, name, n = command[1:]
        t, x, n = map(int, [t, x, n])
    else:
        t = int(command[1])

    queries.append(Query(cmd, t, x, name, n))
    
    # 사람별 주어진 초밥 목록을 관리합니다.
    if cmd == 100:
        if name not in p_queries:
            p_queries[name] = []
        p_queries[name].append(Query(cmd, t, x, name, n))
    # 손님이 입장한 시간과 위치를 관리합니다.
    elif cmd == 200:
        names.add(name)
        entry_time[name] = t
        position[name] = x

# 각 사람마다 자신의 이름이 적힌 조합을 언제 먹게 되는지를 계산하여 해당 정보를 기존 Query에 추가합니다. (111번 쿼리)
for name in names:
    # 해당 사람의 퇴장 시간을 관리합니다.
    # 이는 마지막으로 먹는 초밥 시간 중 가장 늦은 시간이 됩니다.
    exit_time[name] = 0

    for q in p_queries[name]:
        # 만약 초밥이 사람이 등장하기 전에 미리 주어진 상황이라면
        time_to_removed = 0
        if q.t < entry_time[name]:
            # entry_time때의 스시 위치를 구합니다.
            t_sushi_x = (q.x + (entry_time[name] - q.t)) % L
            # 몇 초가 더 지나야 만나는지를 계산합니다.
            additionl_time = (position[name] - t_sushi_x + L) % L

            time_to_removed = entry_time[name] + additionl_time
        # 초밥이 사람이 등장한 이후에 주어졌다면
        else:
            # 몇 초가 더 지나야 만나는지를 계산합니다.
            additionl_time = (position[name] - q.x + L) % L
            time_to_removed = q.t + additionl_time

        # 초밥이 사라지는 시간 중 가장 늦은 시간을 업데이트 합니다.
        exit_time[name] = max(exit_time[name], time_to_removed)

        # 초밥이 사라지는 111번 쿼리를 추가합니다.
        queries.append(Query(111, time_to_removed, -1, name, -1))

# 사람마다 초밥을 마지막으로 먹은 시간 t를 계산하여 그 사람이 해당 t 때 코드트리 오마카세를 떠났다는 Query를 추가합니다. (222번 쿼리)
for name in names:
    queries.append(Query(222, exit_time[name], -1, name, -1))

# 전체 Query를 시간순으로 정렬하되 t가 일치한다면 문제 조건상 사진 촬영에 해당하는 300이 가장 늦게 나오도록 cmd 순으로 오름차순 정렬을 합니다.
# 이후 순서대로 보면서 사람, 초밥 수를 count하다가 300이 나오면 현재 사람, 초밥 수를 출력합니다.
queries.sort(key=lambda q: (q.t, q.cmd))

people_num, sushi_num = 0, 0
for i in range(len(queries)):
    if queries[i].cmd == 100:  # 초밥 추가
        sushi_num += 1
    elif queries[i].cmd == 111:  # 초밥 제거
        sushi_num -= 1
    elif queries[i].cmd == 200:  # 사람 추가
        people_num += 1
    elif queries[i].cmd == 222:  # 사람 제거
        people_num -= 1
    else:  # 사진 촬영시 답을 출력하면 됩니다.
        print(people_num, sushi_num)