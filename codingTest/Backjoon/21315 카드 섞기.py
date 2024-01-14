"""
[21315] 카드 섞기

💛 문제
마술사 영재는 카드 더미를 이용한 마술을 개발하였다.
카드들에는 1부터 N까지의 숫자가 적혀있으며 초기 상태에는 1이 맨 위에 있으며 N개의 카드가 번호 순서대로 쌓여있다.

영재는 마술을 위해 (2, K) - 섞기를 만들었다.
(2, K) - 섞기는 총 K + 1개의 단계로 이루어져있다.
첫 번째 단계는 카드 더미 중 밑에서 2K개의 카드를 더미의 맨 위로 올린다.
이후 i(2 ≤ i ≤ K + 1)번째 단계는 직전에 맨 위로 올린 카드 중 밑에서 2K - i + 1개의 카드를 더미의 맨 위로 올린다.

예를 들어, 카드의 개수가 5개 일 때 초기 상태에서 (2, 2) - 섞기를 하는 과정은 다음과 같다.
(괄호 내에서 왼쪽에 있을수록 위에 있는 카드이다.)
(1, 2, 3, 4, 5) → (2, 3, 4, 5, 1) → (4, 5, 2, 3, 1) → (5, 4, 2, 3, 1)
영재의 마술은 상대방이 초기 상태에서 (2, K) - 섞기를 2번 한 결과를 보고 2번의 (2, K) - 섞기에서 K가 각각 무엇인지 맞추는 마술이다.

마술 아이디어는 생각했지만, K를 알아내는 방법을 모르는 영재를 위해 K를 알아내는 프로그램을 만들자.
2번의 (2, K) - 섞기 후의 카드 더미 결과를 만드는 각각의 K는 유일함이 보장된다.

💚 입력
첫 줄에 N이 주어진다.
둘째 줄에 2번의 (2, K) - 섞기 후의 카드 더미가 위에 있는 카드부터 공백으로 구분하여 주어진다.

💙 출력
첫 번째 K와 두 번째 K를 출력한다.
"""

# n개의 카드, 
# 쌍을 순서대로 모두 검사(카드 섞기)하여 입력 값과 같은 쌍을 찾는 것

def mix( card,  cnt) :
	# 위로 올린 카드들, 현재 위로 올릴 카드 개수
	temp = []
	idx = 0
    i = card - cnt
    for i in range(card)  :
		temp[idx++] = card[i]
		card[i] = 0
	
	for i in range(n)  :
		if (card[i] != 0) : 
			temp[idx++] = card[i]
		card[i] = temp[i]



def solve(k) :
    card = n
    for i in range(k + 2) :
		cnt = pow(2,k - i + 1)
		mix(card, cnt)
		card = cnt

n = int(input())
result = list(map(int, input().split()))

k1 = 1
k2 = 1
card = []
for k1 in range(pow(2, k1), n + 1) :
    for k2 in range(pow(2, k2), n + 1) :
        for i in range(n) :
            card[i] = i + 1
        
        # 섞기 2번씩
        solve(k1)
        solve(k2)
        isFinish = True
        for i in range(n)
            if (result[i] != card[i]) :
                isFinish = False
                break
            
        if (isFinish) :
            print(result)