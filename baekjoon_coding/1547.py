""" 
입력값 : 공의 위치를 바꾼 횟수 <= 50
        x번 y번  (번호들)
        x <= 3, y <= 3, x == y
        
출력 : 공이 있는 컵 번호 (공이 사라져서 컵 밑에 없는 경우에는 -1을 출력한다.)
"""


nums_round = int(input())

ball = 1 

for _ in range(nums_round):
    x, y = map(int, input().split())
    if x > 3 or y > 3:
        print(-1)
    if ball == x:
        ball = y
    elif ball == y:
        ball = x

print(ball)


    




