"""
아이템 줍기

💛 문제
다음과 같은 다각형 모양 지형에서 캐릭터가 아이템을 줍기 위해 이동하려 합니다.
지형은 각 변이 x축, y축과 평행한 직사각형이 겹쳐진 형태로 표현하며, 캐릭터는 이 다각형의 둘레(굵은 선)를 따라서 이동합니다.

만약 직사각형을 겹친 후 다음과 같이 중앙에 빈 공간이 생기는 경우, 다각형의 가장 바깥쪽 테두리가 캐릭터의 이동 경로가 됩니다.
단, 서로 다른 두 직사각형의 x축 좌표 또는 y축 좌표가 같은 경우는 없습니다.
즉, 위 그림처럼 서로 다른 두 직사각형이 꼭짓점에서 만나거나, 변이 겹치는 경우 등은 없습니다.
다음 그림과 같이 지형이 2개 이상으로 분리된 경우도 없습니다.
한 직사각형이 다른 직사각형 안에 완전히 포함되는 경우 또한 없습니다.

지형을 나타내는 직사각형이 담긴 2차원 배열 rectangle, 초기 캐릭터의 위치 characterX, characterY,
아이템의 위치 itemX, itemY가 solution 함수의 매개변수로 주어질 때, 
캐릭터가 아이템을 줍기 위해 이동해야 하는 가장 짧은 거리를 return 하도록 solution 함수를 완성해주세요.

🧡 제한 사항
rectangle의 세로(행) 길이는 1 이상 4 이하입니다.
rectangle의 원소는 각 직사각형의 [좌측 하단 x, 좌측 하단 y, 우측 상단 x, 우측 상단 y] 좌표 형태입니다.
    직사각형을 나타내는 모든 좌표값은 1 이상 50 이하인 자연수입니다.
    서로 다른 두 직사각형의 x축 좌표, 혹은 y축 좌표가 같은 경우는 없습니다.
    문제에 주어진 조건에 맞는 직사각형만 입력으로 주어집니다.
charcterX, charcterY는 1 이상 50 이하인 자연수입니다.
    지형을 나타내는 다각형 테두리 위의 한 점이 주어집니다.
itemX, itemY는 1 이상 50 이하인 자연수입니다.
    지형을 나타내는 다각형 테두리 위의 한 점이 주어집니다.
캐릭터와 아이템의 처음 위치가 같은 경우는 없습니다.
전체 배점의 50%는 직사각형이 1개인 경우입니다.
전체 배점의 25%는 직사각형이 2개인 경우입니다.
전체 배점의 25%는 직사각형이 3개 또는 4개인 경우입니다.

💚 입출력
rectangle	                                characterX	characterY	itemX	itemY	result
[[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]]	1	        3	        7	    8	    17
[[1,1,8,4],[2,2,4,9],[3,6,9,8],[6,3,7,7]]	9	        7	        6	    1	    11
[[1,1,5,7]]	                                1	        1	        4	    7	    9
[[2,1,7,5],[6,4,10,10]]	                    3	        1	        7	    10	    15
[[2,2,5,5],[1,3,6,4],[3,1,4,6]]	            1	        4	        6	    3	    10
"""

from collections import deque

# 지형을 나타내는 직사각형이 담긴 2차원 배열 rectangle, 초기 캐릭터의 위치 characterX, characterY, 아이템의 위치 itemX, itemY
def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0

    # 모든 좌표값은 1 이상 50 이하인 자연수
    graph = [[-1] * 102 for i in range(102)]

    for r in rectangle:
        x1, y1, x2, y2 = r[0] * 2, r[1] * 2, r[2] * 2, r[3] * 2

        for i in range(x1, x2+1):
            for j in range(y1, y2+1):

                # 내부일 때
                if x1 < i < x2 and y1 < j < y2:
                    graph[i][j] = 0
                # 테두리일 때
                elif graph[i][j] != 0:
                    graph[i][j] = 1

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    q = deque()
    
    # 첫 시작
    q.append([characterX * 2, characterY * 2])
    visited = [[0] * 102 for _ in range(102)]
    visited[characterX * 2][characterY * 2] = 1

    # 최단거리 찾기
    while q:
        x, y = q.popleft()

        # 캐릭터와 아이템 위치가 같을 때
        if x == itemX * 2 and y == itemY * 2:
            answer = (visited[x][y] - 1) // 2
            break

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            # 방문도 안했고, 테두리인 경우
            if graph[nx][ny] == 1 and visited[nx][ny] == 0:
                q.append([nx, ny])
                # 최단거리 증가
                visited[nx][ny] = visited[x][y] + 1

    return answer