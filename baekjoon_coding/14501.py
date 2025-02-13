""" 
각각의 상담은 상담을 완료하는데 걸리는 기간 Ti와 상담을 했을 때 받을 수 있는 금액 Pi로 이루어져 있다.
상담을 적절히 했을 때, 백준이가 얻을 수 있는 최대 수익을 구하는 프로그램을 작성하시오.

입력값: 첫째 줄에 N (1 ≤ N ≤ 15)이 주어진다.
둘째 줄부터 N개의 줄에 Ti와 Pi가 공백으로 구분되어서 주어지며, 1일부터 N일까지 순서대로 주어진다. (1 ≤ Ti ≤ 5, 1 ≤ Pi ≤ 1,000)

7
3 10
5 20
1 10
1 20
2 15
4 40
2 200

출력값: 백준이가 얻을 수 있는 최대 이익을 출력한다.
"""
import sys

N = int(sys.stdin.readline())

schedules = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]

dp = [0] * (N + 1) 

for i in range(N-1, -1, -1):
    time, money = schedules[i]
    end_day = i + time

    if end_day<= N:
        dp[i] = max(dp[i + 1], dp[end_day] + money) 
    else:
        dp[i] = dp[i + 1] 

print(dp[0])