# MN 단위의 정사각형 (8 <= M and N <= 50)
# 8x8 크기의 체스판을 만들어야 하는데 
# 변을 공유하는 두 개의 사각형의 색이 달라야한다 
# e.g BWBWBWBW
#     WBWBWBWB
#     BWBWBWBW

# 테스트 코드
def minor_testing(arr):
    cnt= 0

    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[i][j] == arr[i][j+1]:
                if arr[i][j+1] == "B":
                    arr[i][j+1] = "W"
                else:
                    arr[i][j+1] = "B"
                cnt += 1
            else:
                continue
    
    return cnt


test_arr = [['W','B','W','B','W','B','W','B'],
            ['B','W','B','W','B','W','B','W'],
            ['W','B','W','B','W','B','W','B'],
            ['B','W','B','B','B','W','B','W'],
            ['W','B','W','B','W','B','W','B'],
            ['B','W','B','W','B','W','B','W'],
            ['W','B','W','B','W','B','W','B'],
            ['B','W','B','W','B','W','B','W']]


# 백준
# 입력값을 받기
import sys

N,M = map(int, sys.stdin.readline().split())

# 받은 입력값을 리스트로 바꿔주기 N행 만큼
board = []
for _ in range(N):
    board.append(input())

# 시작점을 인덱스 0에서 N-7까지 (시작점을 0부터 N-7까지 바꿀 수 있음)
# 시작점을 인덱스 0에서 M-7까지 바꿔줌 (시작점을 0부터 M-7까지 바꿀 수 있음)
def find_min_count(board, N, M):
    min_count = 10000

    for n in range(N-7):
        for m in range(M-7):
            min_count = min(min_count, count_min_colors(board, n, m))
    return min_count


def count_min_colors(board, x, y):
    color_w = 0
    color_b = 0

    for i in range(8):
        for j in range(8):
            # 짝수 인덱스 색 찾기 
            if (i + j) % 2 == 0:
                # 짝수 인덱스가 흰색 일 경우
                if board[x + i][y + j] != 'W':
                    color_w += 1
                # 짝수 인덱스가 검은색 일 경우
                if board[x + i][y + j] != 'B':
                    color_b += 1
            else:
                # 홀수 인덱스가 검은색 일 경우
                if board[x + i][y + j] != 'B':
                    color_w += 1
                # 홀수 인덱스가 흰색 일 경우
                if board[x + i][y + j] != 'W':
                    color_b += 1

    return min(color_w, color_b)


print(find_min_count(board, N, M))
