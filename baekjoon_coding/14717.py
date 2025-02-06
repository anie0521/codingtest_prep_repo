# 1 ~ 10 카드 * 2 장씩 = 20 장, 2명 참가
# 참가자는 순서대로 20장 중에서 무작위로 2장 카드를 가져옴
# 상대방이 있는 중복 카드 x, 자기 자신의 카드만 알고 상대방의 카드는 모름
# 강한 족보의 패 -> 승, 같은 족보의 패 -> 무승부

# 2장을 가져왔을때 두 패가 같으면 n땡 -> e.g. 두 패가 모두 10 -> 10 땡, 두 패가 모두 6 -> 6땡
# 다른 두 패를 가져왔을때 합친 수가 n 일때 n 끗 -> e.g. 두 패를 더했을 때 일의 자리수가 9 -> 9 끗
# 더했을 때 일의 자리수가 0 -> 0 끗 (1, 9)(2, 8)(3, 7)(4, 6)
# 10땡 > 9 ~ 2 땡> 1땡 > 9끗 > 8 ~ 1 끗> 0 끗 (강한 패 순) 

# 구해야하는 것 : 상대를 이길 확률 (소수점 이하 셋 째 자리까지 반올림)
# 출력값이 0.700 이면 0.700까지 출력 0.7은 오답

# 조합 공식 사용 -> n개 중에 r개를 뽑는다(순서 상관없음) = nCr = n! / (n-r)!r! -> (n! 을 r 갯수만큼 곱하고) / r!

# 2장을 뽑고 카드는 18장 남고 -> 모든 케이스는 18 * 17 / 2 = 153
# 땡을 뽑으면 나보다 강한 땡의 개수를 센뒤에 -> 내가 뽑은 a, 강한 땡의 수 10 - a
# 1 - ((10 - a)/153)
# 끗을 뽑으면 내가 이길 끗들 의 경우의 수 m 을 구함 -> m / 153 
# e.g. 1, 2 -> 3 끗  그러면 0 끗(x), 1 끗(y), 2(z) 끗 의 경우의 수의 합 m = x + y + z
# m / 153 

# vs code 형식
def cal_win_probability(a, b):
    # 소수 3번째 자리
    formatted = "{:.3f}".format

    # 2장을 뺀 18장의 조합
    total_case = 18 * 17 / 2
    
    # 20장 중에 2장을 뺀 모든 카드 개수
    cards = [i for i in range(1, 11)] * 2
    
    # 카드 2장을 뺌
    cards.remove(a)
    cards.remove(b)

    # 땡일 떄
    if a == b:
        equal_res = round(1 - ((10 - a) / total_case), 3)
        # print(formatted(equal_res))
        return formatted(equal_res)

    # 끗일 때    
    else:
        winning = 0

        for i in range(len(cards)):
            for j in range(i + 1, len(cards)):
                # 두 카드는 같으면 안됨 (땡이면 안됨) 그리고 일의 자리수가 뽑은 끗 값보다 작아야 됨
                if cards[i] != cards[j] and ((cards[i] + cards[j]) % 10) < ((a + b) % 10):
                    winning += 1
        
        diff_res = round(winning / total_case, 3)
        # print(formatted(diff_res))
        return formatted(diff_res)

print("test 1: ", cal_win_probability(1,1))
print("test 2: ", cal_win_probability(1,2))
print("test 3: ", cal_win_probability(1,9))
print("test 4: ", cal_win_probability(10,10))


# 백준
import sys
input = sys.stdin.readline

a, b = input().split()

def cal_win_probability(a, b):
    # 소수 3번째 자리
    formatted = "{:.3f}".format

    # 2장을 뺀 18장의 조합
    total_case = 18 * 17 / 2
    
    # 20장 중에 2장을 뺀 모든 카드 개수
    cards = [i for i in range(1, 11)] * 2

    a = int(a)
    b = int(b)
    
    # 카드 2장을 뺌
    cards.remove(a)
    cards.remove(b)

    # 땡일 떄
    if a == b:
        equal_res = round(1 - ((10 - a) / total_case), 3)
        # print(formatted(equal_res))
        return formatted(equal_res)

    # 끗일 때    
    else:
        winning = 0

        for i in range(len(cards)):
            for j in range(i + 1, len(cards)):
                # 두 카드는 같으면 안됨 (땡이면 안됨) 그리고 일의 자리수가 뽑은 끗 값보다 작아야 됨
                if cards[i] != cards[j] and ((cards[i] + cards[j]) % 10) < ((a + b) % 10):
                    winning += 1
        
        diff_res = round(winning / total_case, 3)
        # print(formatted(diff_res))
        return formatted(diff_res)
    
print(cal_win_probability(a, b))