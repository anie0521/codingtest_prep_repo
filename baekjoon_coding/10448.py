""" 
백준 10448번
자연수 n에 대해 n ≥ 1의 삼각수 Tn는 명백한 공식이 있다.

Tn = 1 + 2 + 3 + ... + n = n(n+1)/2

1796년, 가우스는 모든 자연수가 최대 3개의 삼각수의 합으로 표현될 수 있다고 증명하였다. 예를 들어,

4 = T1 + T2
5 = T1 + T1 + T2
6 = T2 + T2 or 6 = T3
10 = T1 + T2 + T3 or 10 = T4
이 결과는 증명을 기념하기 위해 그의 다이어리에 “Eureka! num = Δ + Δ + Δ” 라고 적은것에서 유레카 이론으로 알려졌다. 꿍은 몇몇 자연수가 정확히 3개의 삼각수의 합으로 표현될 수 있는지 궁금해졌다. 위의 예시에서, 5와 10은 정확히 3개의 삼각수의 합으로 표현될 수 있지만 4와 6은 그렇지 않다.

자연수가 주어졌을 때, 그 정수가 정확히 3개의 삼각수의 합으로 표현될 수 있는지 없는지를 판단해주는 프로그램을 만들어라. 단, 3개의 삼각수가 모두 달라야 할 필요는 없다.

입력 -> 프로그램은 표준입력을 사용한다. 테스트케이스의 개수는 입력의 첫 번째 줄에 주어진다. 각 테스트케이스는 한 줄에 자연수 K (3 ≤ K ≤ 1,000)가 하나씩 포함되어있는 T개의 라인으로 구성되어있다.

출력 -> 프로그램은 표준출력을 사용한다. 각 테스트케이스에대해 정확히 한 라인을 출력한다. 만약 K가 정확히 3개의 삼각수의 합으로 표현될수 있다면 1을, 그렇지 않다면 0을 출력한다.

백준 예제 입력값
3
10
20
1000

출력값
1
0
1
"""

# 개념 정리 
# 테스트 케이스에 있는 삼각수의 합의 자연수는 3 ≤ K ≤ 1,000
# 따라서 Ti + Tj + Ta <= 1000 
# K는 꼭 3개의 T의 합이여야한다. 그러나 그 합이 1000 이상이면 안됨.

# 첫번째 시도
# def eureka(k):
#     triangles = []
#     n = 1

#     while (n * (n + 1) // 2) <= 1000:
#         t = n * (n + 1) // 2
#         triangles.append(t)
#         n += 1

#     for i in triangles:
#         for j in triangles:
#             for a in triangles:
#                 if i + j + a == k:
#                     return 1
#                 else:
#                     return 0


# print(eureka(20))

# 백준
import sys

input = sys.stdin.readline

def is_eureka(k):
    triangles = []
    n = 1
    res = []

    while (n * (n + 1) // 2) <= 1000:
        t = n * (n + 1) // 2
        triangles.append(t)
        n += 1

    for i in triangles:
        for j in triangles:
            for a in triangles:
                sum_tri = i + j + a
                if sum_tri == k and sum_tri <= 1000:
                    return 1
    return 0

num_tc = int(input())

for _ in range(num_tc):
    k = int(input())
    print(is_eureka(k))