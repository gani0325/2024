from collections import deque

# 좌표를 나타내는 클래스
class Point:
    def __init__(self, row, col):
        self.row = row
        self.col = col

# 미로에서 모든 경로 찾기
def find_all_paths(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    paths = []
    visited = [[False] * cols for _ in range(rows)]

    def dfs(current, path):
        nonlocal paths
        visited[current.row][current.col] = True
        path.append(Point(current.row, current.col))

        if current.row == end.row and current.col == end.col:
            paths.append(path.copy())
        else:
            dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]
            for i in range(4):
                new_row, new_col = current.row + dr[i], current.col + dc[i]
                if 0 <= new_row < rows and 0 <= new_col < cols and maze[new_row][new_col] != '#' and not visited[new_row][new_col]:
                    dfs(Point(new_row, new_col), path)

        visited[current.row][current.col] = False
        path.pop()

    dfs(start, [])
    return paths

# 미로 출력 함수 (경로 '*'로 표시)
def print_maze_with_paths(maze, paths):
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            current = Point(i, j)
            is_on_path = any(current in path for path in paths)

            if is_on_path:
                print("*", end=" ")
            else:
                print(maze[i][j], end=" ")
        print()

# 시작점과 끝점
start = Point(0, 1)
end = Point(8, 8)

def read_maze_from_file(filename):
    global start, end
    maze = []

    try:
        with open(filename, 'r') as file:
            j = 0
            for line in file:
                row = list(line.strip())
                maze.append(row)
                for i in range(254) :
                    if row[i] == 'S' :
                        start = Point(j, i)
                    elif row[i] == 'G' :
                        end = Point(j, i)
                j += 1
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return maze

# 파일에서 미로 읽어오기
file_path = 'maze.txt'  # 파일 경로를 실제 파일 경로로 변경해주세요
maze = read_maze_from_file(file_path)

# 읽어온 미로 출력
if maze:
    print("Read maze from file:")
    for row in maze:
        print(' '.join(row))
else:
    print("Failed to read the maze from file.")




# 모든 경로 찾기
all_paths = find_all_paths(maze, start, end)

if all_paths:
    print("모든 가능한 경로:")
    for i, path in enumerate(all_paths, start=1):
        print(f"경로 {i}: {path}")
    print("\n미로 출력:")
    print_maze_with_paths(maze, all_paths)
else:
    print("목표 지점에 도달할 수 없습니다.")
