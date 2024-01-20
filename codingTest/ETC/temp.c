#include <stdio.h>
#include <stdlib.h>

#define MAX_ROWS 10
#define MAX_COLS 10

// 좌표를 나타내는 구조체
typedef struct
{
    int row;
    int col;
} Point;

// 큐를 위한 구조체
typedef struct
{
    Point *array;
    int front;
    int rear;
    int capacity;
} Queue;

// 동적 배열을 나타내는 구조체
typedef struct
{
    Point *data;
    size_t size;
    size_t capacity;
} DynamicArray;

// 큐 초기화
Queue *initializeQueue(int capacity)
{
    Queue *queue = (Queue *)malloc(sizeof(Queue));
    queue->array = (Point *)malloc(capacity * sizeof(Point));
    queue->front = 0;
    queue->rear = -1;
    queue->capacity = capacity;
    return queue;
}

// 큐에 원소 삽입
void enqueue(Queue *queue, Point point)
{
    if (queue->rear == queue->capacity - 1)
    {
        printf("큐가 가득 찼습니다.\n");
        return;
    }
    queue->array[++(queue->rear)] = point;
}

// 큐에서 원소 제거
Point dequeue(Queue *queue)
{
    if (queue->front > queue->rear)
    {
        printf("큐가 비어있습니다.\n");
        Point emptyPoint = {-1, -1};
        return emptyPoint;
    }
    return queue->array[(queue->front)++];
}

// 큐 메모리 해제
void freeQueue(Queue *queue)
{
    free(queue->array);
    free(queue);
}

// 동적 배열 초기화
DynamicArray initializeDynamicArray()
{
    DynamicArray array;
    array.data = NULL;
    array.size = 0;
    array.capacity = 0;
    return array;
}

// 동적 배열에 요소 추가
void appendToDynamicArray(DynamicArray *array, Point element)
{
    if (array->size == array->capacity)
    {
        array->capacity = (array->capacity == 0) ? 1 : array->capacity * 2;
        array->data = realloc(array->data, array->capacity * sizeof(Point));

        if (array->data == NULL)
        {
            perror("메모리 할당 실패");
            exit(EXIT_FAILURE);
        }
    }

    array->data[array->size++] = element;
}

// 동적 배열 메모리 해제
void freeDynamicArray(DynamicArray *array)
{
    free(array->data);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
}

// 미로에서 최단 경로 길이 찾기
int findShortestPathLength(char maze[MAX_ROWS][MAX_COLS], int rows, int cols, Point start, Point end, DynamicArray *shortestPath)
{
    int visited[MAX_ROWS][MAX_COLS] = {0};
    Queue *queue = initializeQueue(rows * cols);

    enqueue(queue, start);
    visited[start.row][start.col] = 1;

    int dr[] = {-1, 1, 0, 0};
    int dc[] = {0, 0, -1, 1};

    while (queue->front <= queue->rear)
    {
        Point current = dequeue(queue);

        if (current.row == end.row && current.col == end.col)
        {
            freeQueue(queue);
            return visited[current.row][current.col] - 1;
        }

        for (int i = 0; i < 4; i++)
        {
            int newRow = current.row + dr[i];
            int newCol = current.col + dc[i];

            if (newRow >= 0 && newRow < rows && newCol >= 0 && newCol < cols &&
                maze[newRow][newCol] != '#' && !visited[newRow][newCol])
            {
                Point next = {newRow, newCol};
                enqueue(queue, next);
                visited[newRow][newCol] = visited[current.row][current.col] + 1;
                appendToDynamicArray(shortestPath, next);
            }
        }
    }

    freeQueue(queue);
    return -1;
}

// 미로 출력 함수 (최단 경로 '*'로 표시)
void printMazeWithPath(char maze[MAX_ROWS][MAX_COLS], int rows, int cols, DynamicArray *path)
{
    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j < cols; j++)
        {
            Point current = {i, j};
            int isOnPath = 0;

            // 현재 위치가 최단 경로에 속하는지 확인
            for (size_t k = 0; k < path->size; k++)
            {
                if (current.row == path->data[k].row && current.col == path->data[k].col)
                {
                    isOnPath = 1;
                    break;
                }
            }

            if (isOnPath)
            {
                printf("* ");
            }
            else
            {
                printf("%c ", maze[i][j]);
            }
        }
        printf("\n");
    }
}

int main()
{
    FILE *fp;
    // 파일 열기
    fp = fopen("maze.txt", "rt");
    if (fp == NULL)
    {
        printf("File not found\n");
        return 0;
    }

    char maze[MAX_ROWS][MAX_COLS];

    // 파일로부터 데이터 입력 받아 노드 삽입
    int j = 0;
    Point start;
    Point end;

    while (!feof(fp))
    {
        // feof는 파일 포인터가 마지막에 있는지 검사 (마지막이면 0 반환)
        // 반복문으로, 텍스트 파일을 한 줄씩 읽다가 다 읽으면 종료한다
        char str[254];
        fgets(str, 254, fp);
        for (int i = 0; i < 254; i++)
        {
            maze[j][i] = str[i];

            // 출발지는 ‘S’이며, 목적지는 ‘G’
            if (str[i] == 'S')
            {
                start.col = i;
                start.row = j; // 시작점 좌표
                printf("%d %d\n", start.row, start.col);
            }
            else if (str[i] == 'G')
            {
                end.col = i;
                end.row = j; // 목표점 좌표
                printf("%d %d\n", end.row, end.col);
            }
        }
        j += 1;
    }
    int rows = MAX_ROWS;
    int cols = MAX_COLS;
    DynamicArray shortestPath = initializeDynamicArray();
    int shortestPathLength = findShortestPathLength(maze, rows, cols, start, end, &shortestPath);

    if (shortestPathLength != -1)
    {
        printf("최단 경로의 길이: %d\n", shortestPathLength);
        printf("최단 경로:\n");
        printMazeWithPath(maze, rows, cols, &shortestPath);
    }
    else
    {
        printf("목표 지점에 도달할 수 없습니다.\n");
    }

    // 메모리 해제
    freeDynamicArray(&shortestPath);

    return 0;
}