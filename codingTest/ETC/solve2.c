// fopen 함수는 안전성 문제로 비활성화됨
#pragma warning(disable : 4996)
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MAX_ROWS 254
#define MAX_COLS 254

typedef struct
{
    int row;
    int col;
} Point;

// 2차원 배열에 저장
void fileToList(char maze[MAX_ROWS][MAX_COLS], const char *filename, int *rows, int *cols)
{
    FILE *file = fopen(filename, "r");
    if (file == NULL)
    {
        perror("파일 열기 실패");
        exit(EXIT_FAILURE);
    }

    *rows = 0;
    *cols = 0;

    while (fgets(maze[*rows], MAX_COLS, file) != NULL)
    {
        (*rows)++;
        *cols = strlen(maze[0]) - 1;
    }

    fclose(file);
}

// 미로 출력 & 출발점과 도착점 찾기
Point start;
Point end;
void printMaze(char maze[MAX_ROWS][MAX_COLS], int rows, int cols)
{
    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j < cols; j++)
        {
            printf("%c", maze[i][j]);

            if (maze[i][j] == 'S')
            {
                start.row = i;
                start.col = j;
            }
            else if (maze[i][j] == 'G')
            {
                end.row = i;
                end.col = j;
            }
        }
        printf("\n");
    }

    printf("start : %d %d\n", start.row, start.col);
    printf("end : %d %d\n", end.row, end.col);
}

int main()
{
    char maze[MAX_ROWS][MAX_COLS];
    int rows, cols;

    // 파일에서 미로 읽어오기
    fileToList(maze, "maze.txt", &rows, &cols);

    // 읽어온 미로 출력
    if (rows >= 0 && cols >= 0)
    {
        printf("Read maze from file:\n");
        printMaze(maze, rows, cols);
    }
    else
    {
        printf("Failed to read the maze from file.\n");
    }

    return 0;
}