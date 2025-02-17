"""
자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열

입력: 첫째 줄에 자연수 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)

출력: 한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.
수열은 사전 순으로 증가하는 순서로 출력해야 한다.
"""
import sys

def backtrack(N, M, current, used):
    # 현재 수열의 길이가 M이면 출력
    if len(current) == M:
        print(" ".join(map(str, current)))
        return
    
    for i in range(1, N + 1):
        # 이미 사용된 수는 제외
        if not used[i]:
            used[i] = True
            current.append(i)
            backtrack(N, M, current, used)  # 다음 숫자 고르기
            current.pop()  # 백트래킹: 마지막 수를 빼고 다시 시도
            used[i] = False  # 사용한 수를 되돌림


N, M = map(int, sys.stdin.readline().split())

# 사용 여부를 기록할 리스트
used = [False] * (N + 1)
current = []

# 백트래킹 함수 호출
backtrack(N, M, current, used)
