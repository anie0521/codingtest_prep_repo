"""  
축구를 재미있게 하기 위해서 스타트 팀의 능력치와 링크 팀의 능력치의 차이를 최소로 하려고 한다. 위의 예제와 같은 경우에는 
1, 4번이 스타트 팀, 2, 3번 팀이 링크 팀에 속하면 스타트 팀의 능력치는 6, 링크 팀의 능력치는 6이 되어서 차이가 0이 되고 이 값이 최소이다.

입력 : 첫째 줄에 N(4 ≤ N ≤ 20, N은 짝수)이 주어진다. 둘째 줄부터 N개의 줄에 S가 주어진다. 각 줄은 N개의 수로 이루어져 있고, 
i번 줄의 j번째 수는 Sij 이다. Sii는 항상 0이고, 나머지 Sij는 1보다 크거나 같고, 100보다 작거나 같은 정수이다.

출력 : 스타트 팀과 링크 팀의 능력치의 차이의 최솟값을 출력한다.
"""

import sys
from itertools import combinations

N = int(sys.stdin.readline())

skills = [list(map(int, input().split())) for _ in range(N)]

def cal_score(team, skills):
    score = 0
    for i in range(len(team)):
        for j in range(i + 1, len(team)):
            score += skills[team[i]][team[j]] + skills[team[j]][team[i]]
    
    return score


def find_min_diff(N, skills):
    players = list(range(N))

    min_diff = float('inf')

    # 반은 스타트 반은 링크
    half = N // 2

    for start_team in combinations(players, half):   #스타트 팀의 조합 생성
        link_team = [player for player in players if player not in start_team]     #링크 팀의 조합 생성

        start_score = cal_score(start_team, skills)
        link_score = cal_score(link_team, skills)

        diff = abs(start_score - link_score)      #두 팀의 차

        min_diff = min(min_diff, diff)            #차이 중에서 최솟값

    
    return min_diff


res = find_min_diff(N, skills)

print(res)