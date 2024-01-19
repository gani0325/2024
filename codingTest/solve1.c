// fopen 함수는 안전성 문제로 비활성화됨
#pragma warning(disable : 4996)
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#define MAX_LEN 100

// double linked list 구조체
typedef struct Node
{
    // 내용
    char data[100];
    // 길이, 대문자 개수, 숫자 대소문자 제외한 개수
    int length;
    int uppercase;
    int etc;
    struct Node *prev;
    struct Node *next;
} Node;

// double linked list 생성
Node *createNode(char data[])
{
    Node *newNode = (Node *)malloc(sizeof(Node));
    if (newNode != NULL)
    {
        // 대문자, 소문자, 숫자
        int aA = 0, aa = 0, aN = 0;
        for (int i = 0; i < strlen(data); i++)
        {
            if (data[i] >= 'A' && data[i] <= 'Z')
                aA++;

            else if (data[i] >= 'a' && data[i] <= 'z')
                aa++;

            else if (data[i] >= '0' && data[i] <= '9')
                aN++;
        }

        // 구조체에 내용, 길이, 대문자 개수, 숫자와 대소문자 제외 개수
        strcpy(newNode->data, data);

        // strlen 해도 문자열의 개수가 2개씩 크게 나옴 (이유는 모르겠음 -> -2 를 추가로 해줌)
        newNode->length = strlen(data) - 2;
        newNode->uppercase = aA;
        newNode->etc = strlen(data) - aA - aa - aN - 2;

        newNode->prev = NULL;
        newNode->next = NULL;
    }
    return newNode;
}

// 이중 연결 리스트에 노드를 삽입
void insertNode(Node **head, char data[])
{
    Node *newNode = createNode(data);

    if (*head == NULL)
    {
        *head = newNode;
        return;
    }

    // 노드 삽입
    Node *current = *head;
    while (current->next != NULL)
    {
        current = current->next;
    }

    newNode->prev = current;
    current->next = newNode;
}

// 이중 연결 리스트를 출력
void displayList(Node *head)
{
    while (head != NULL)
    {
        printf("%3d, %3d, %3d %s\n",
               head->length, head->uppercase, head->etc, head->data);

        head = head->next;
    }
}

// 이중 연결 리스트를 아스키 코드로 정렬
void sortedList(Node **head)
{
    if (*head == NULL || (*head)->next == NULL)
    {
        return;
    }

    Node *sorted = NULL;
    Node *current = *head;

    while (current != NULL)
    {
        Node *next = current->next;

        if (sorted == NULL || strcmp(current->data, sorted->data) < 0)
        {
            // 정렬된 리스트의 맨 앞에 삽입
            current->prev = NULL;
            current->next = sorted;
            if (sorted != NULL)
            {
                sorted->prev = current;
            }
            sorted = current;
        }
        else
        {
            Node *temp = sorted;
            while (temp->next != NULL && strcmp(current->data, temp->next->data) >= 0)
            {
                temp = temp->next;
            }

            current->prev = temp;
            current->next = temp->next;

            if (temp->next != NULL)
            {
                temp->next->prev = current;
            }
            temp->next = current;
        }

        current = next;
    }

    *head = sorted;
}

// 마지막 문자열 만 잘 나옴 (이유는 모르겠음 -> 마지막만 원래대로 함)
void updateList(Node *head)
{
    if (head == NULL)
    {
        return;
    }

    Node *last = head;
    while (last->next != NULL)
    {
        last = last->next;
    }
    // 위에 노드 추가할 때 전체 -2 했으므로, 마지막 노드만 +2 다시 원상복구
    last->length += 2;
    last->etc += 2;
}

// 메모리 해제
void freeList(Node *head)
{
    while (head != NULL)
    {
        Node *temp = head;
        head = head->next;
        free(temp);
    }
}

int main()
{
    Node *head = NULL;

    FILE *fp;
    // 파일 열기
    fp = fopen("python.txt", "rt");
    if (fp == NULL)
    {
        printf("File not found\n");
        return 0;
    }

    // 파일로부터 데이터 입력 받아 노드 삽입
    while (!feof(fp))
    {
        // feof는 파일 포인터가 마지막에 있는지 검사 (마지막이면 0 반환)
        // 반복문으로, 텍스트 파일을 한 줄씩 읽다가 다 읽으면 종료한다
        char str[MAX_LEN];
        fgets(str, MAX_LEN, fp);
        // printf("%ld ", strlen(str));
        // printf(" : %s", str);

        insertNode(&head, str); // head에 새로 만든 str을 insert
    }

    // 마지막 줄만 다시 +2 하겠음
    updateList(head);

    // "내용" 으로 아스키 코드로 정렬
    sortedList(&head);

    // 정렬된 리스트 출력
    displayList(head);

    // 메모리 해제
    freeList(head);

    return 0;
}