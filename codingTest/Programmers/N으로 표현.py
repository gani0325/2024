"""
N으로 표현

💛 문제
아래와 같이 5와 사칙연산만으로 12를 표현할 수 있습니다.

12 = 5 + 5 + (5 / 5) + (5 / 5)
12 = 55 / 5 + 5 / 5
12 = (55 + 5) / 5
5를 사용한 횟수는 각각 6,5,4 입니다. 그리고 이중 가장 작은 경우는 4입니다.

이처럼 숫자 N과 number가 주어질 때, 
N과 사칙연산만 사용해서 표현 할 수 있는 방법 중 N 사용횟수의 최솟값을 return 하도록 solution 함수를 작성하세요.

🧡 제한 사항
N은 1 이상 9 이하입니다.
number는 1 이상 32,000 이하입니다.
수식에는 괄호와 사칙연산만 가능하며 나누기 연산에서 나머지는 무시합니다.
최솟값이 8보다 크면 -1을 return 합니다.

💚 입출력
N	number	return
5	12	    4
2	11	    3
"""

def solution(N, number):
    num = [] # 숫자 조합을 담는 리스트
    
    for i in range(1, 9):
        temp = set()
        temp.add(int(str(N)*i)) # 이어붙이는 경우의 수
        
        # 숫자 조합끼리의 사칙연산
        for j in range(0, i-1):  
            for x in num[j]:    # (1, n-1) 부터 (n-1, 1)까지
                for y in num[-j-1]:
                    temp.add(x + y)
                    temp.add(x - y)
                    temp.add(x * y)
                    # 0 으로 안나눠짐
                    if x != 0 :
                        temp.add(y // x)
                    if y != 0 :
                        temp.add(x // y)
        
        # 숫자 조합에 number 가 있는 경우
        if number in temp:
            return i
        
        # 숫자 조합에 number 가 없으면 리스트에 추가
        num.append(temp)
        
    return -1