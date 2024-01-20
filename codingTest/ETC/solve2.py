from queue import Queue


class Point:
    def __init__(self, row, col):
        self.row = row
        self.col = col

def read_maze_from_file(filename):
    with open(filename, 'r') as file:
        maze = [list(line.strip()) for line in file]  # 문자열을 리스트로 변경
    rows, cols = len(maze), len(maze[0])
    return maze, rows, cols

def print_maze_with_path(maze, path):
    for i, row in enumerate(maze):
        for j, cell in enumerate(row):
            current = Point(i, j)
            is_on_path = any(current.row == p.row and current.col == p.col for p in path)

            if is_on_path:
                print('* ', end='') if maze[current.row][current.col] == ' ' else print(maze[current.row][current.col] + ' ', end='')
            else:
                print(cell + ' ', end='')

        print()

def find_shortest_path(maze, start, end):
    visited = [[False] * len(maze[0]) for _ in range(len(maze))]
    queue = Queue()

    queue.put(start)
    visited[start.row][start.col] = True

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    while not queue.empty():
        current = queue.get()

        for i in range(4):
            new_row = current.row + dr[i]
            new_col = current.col + dc[i]

            if 0 <= new_row < len(maze) and 0 <= new_col < len(maze[0]) and maze[new_row][new_col] != '#' and not visited[new_row][new_col]:
                next_point = Point(new_row, new_col)
                queue.put(next_point)
                visited[new_row][new_col] = True

                if next_point.row == end.row and next_point.col == end.col:
                    return True

    return False

def find_shortest_path_length(maze, start, end):
    visited = [[0] * len(maze[0]) for _ in range(len(maze))]
    queue = Queue()

    queue.put(start)
    visited[start.row][start.col] = 1

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    while not queue.empty():
        current = queue.get()

        for i in range(4):
            new_row = current.row + dr[i]
            new_col = current.col + dc[i]

            if 0 <= new_row < len(maze) and 0 <= new_col < len(maze[0]) and maze[new_row][new_col] != '#' and not visited[new_row][new_col]:
                next_point = Point(new_row, new_col)
                queue.put(next_point)
                visited[new_row][new_col] = visited[current.row][current.col] + 1

                if next_point.row == end.row and next_point.col == end.col:
                    return visited[next_point.row][next_point.col] - 1

    return -1

def main():
    maze, rows, cols = read_maze_from_file("maze.txt")

    if rows > 0 and cols > 0:
        print("Read maze from file:")
        for row in maze:
            print(''.join(row))
        print()

        # Find start and end points
        start = None
        end = None

        for i in range(rows):
            for j in range(cols):
                if maze[i][j] == 'S':
                    start = Point(i, j)
                elif maze[i][j] == 'G':
                    end = Point(i, j)

        if start is not None and end is not None:
            if find_shortest_path(maze, start, end):
                shortest_path_length = find_shortest_path_length(maze, start, end)
                print("\n최단 경로의 길이:", shortest_path_length)
                print("최단 경로:")
                print_maze_with_path(maze, [start, end])  # 시작과 끝점만 넘겨주어 최단 경로 표시
            else:
                print("\n목표 지점에 도달할 수 없습니다.")
        else:
            print("출발점 또는 도착점이 미로에 없습니다.")
    else:
        print("Failed to read the maze from file.")

if __name__ == "__main__":
    main()
