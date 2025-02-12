""" 
입력값 : 5 x 5 빙고판, 5 x 5 사회자 답 빙고판 
11 12 2 24 10 (내 빙고판)
16 1 13 3 25
6 20 5 21 17
19 4 8 14 9
22 15 7 23 18  (내 빙고판)
5 10 7 16 2    (사회자 빙고판)
4 22 8 17 13
3 18 1 6 25
12 19 23 14 21
11 24 9 20 15  (사회자 빙고판)

빙고판의 숫자는 <= 25

사회자가 부를때 3 빙고가 만들어지면 몇 번째 수를 부른 후 철수가 "빙고"를 외치게 되는지 출력한다

빙고가 이뤄질 패턴

가로선 
세로선 
대각선 x 모양 (왼쪽 위 -> 오른쪽 아래), (오른쪽 위 -> 왼쪽 아래)
"""
import sys

# 빙고판 입력 (5x5)
board_list = [list(map(int, sys.stdin.readline().split())) for _ in range(5)]

# 사회자가 부르는 숫자 입력 (5x5)
call_list = [list(map(int, sys.stdin.readline().split())) for _ in range(5)]

# 사회자가 부르는 2차원배열을 1차원으로 바꿈
call = sum(call_list, [])

# 빙고판을 딕셔너리로 정리 -> 숫자 : 2차 배열 위치 i, j
board = {}

for i in range(5):
    for j in range(5):
        board[board_list[i][j]] = (i, j)

checked_rows = [0] * 5
checked_cols = [0] * 5
checked_diag_right_to_left = 0
checked_diag_left_to_right = 0
cnt = 0


for idx, num in enumerate(call):
    if num in board:
        row, col = board[num]

        checked_rows[row] += 1
        checked_cols[col] += 1

        if checked_rows[row] == 5:
            cnt += 1
            checked_rows[row] = 6

        if checked_cols[col] == 5:
            cnt += 1
            checked_cols[col] == 6


        if row == col:
            checked_diag_left_to_right += 1

            if checked_diag_left_to_right == 5:
                cnt += 1
                checked_diag_left_to_right = 6

        if row + col == 4:
            checked_diag_right_to_left += 1

            if checked_diag_right_to_left == 5:
                cnt += 1
                checked_diag_right_to_left = 6
        
    if cnt >= 3:
        print(idx + 1)
        break  