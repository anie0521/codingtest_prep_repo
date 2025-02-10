""" 
입력값 첫쨰줄: 현재 보유 하고 있는 현금

두 번째 줄: 2021년 1월 1일부터 2021년 1월 14일까지의 MachineDuck 주가가 공백을 두고 
차례대로 주어진다. 모든 입력은 1000 이하의 양의 정수이다.

출력 -> 1월 14일 기준 준현이의 자산이 더 크다면 "BNP"를, 성민이의 자산이 더 크다면 "TIMING"을 출력한다.

둘의 자산이 같다면 "SAMESAME"을 출력한다. 모든 결과 따옴표를 제외하고 출력한다.

준현이는 살 수 있을때 다 사는 방법
성민이는 3일 연속 상승 → 주식을 전량 매도 / 3일 연속 하락 → 매수 가능한 만큼 주식 매수


성민이는 1-3일차에서 상승인지 하락인지 체크후 4일차에서 3일 차의 가격과 4일 차의 가격과 비교후 매수 결정
"""


import sys

buying_power = int(sys.stdin.readline())

stock_arr = list(map(int, input().split()))



def bnp_investment(stocks, money):
    j_stock = 0
    j_money = money
    
    for i in range(len(stocks)):
        if stocks[i] <= j_money:
            j_stock = money // stocks[i]
            j_money -= stocks[i] * j_stock
    
    j_money += stocks[-1] * j_stock
    
    return j_money


def timing_investment(stocks, money):
    s_money = money
    s_stock = 0

    for i in range(2, len(stocks) - 1):
        # 3일 연속 하락이면 매수 -> 4 일차 주식 삼 
        if stocks[i] <= stocks[i - 1] and stocks[i - 1] <= stocks[i - 2]:
            if s_money >= stocks[i] and stocks[i] >= stocks[i+1]:  # 주식을 살 수 있으면
                available = s_money // stocks[i+1] 
                s_stock += available 
                s_money -= available * stocks[i+1]  

        # 3일 연속 상승이면 매도 -> 4 일차 주식 매도
        if stocks[i] > stocks[i - 1] and stocks[i - 1] > stocks[i - 2]:
            if stocks[i] <= stocks[i+1]:
                if s_stock: 
                    s_money += s_stock * stocks[i+1] 
                    s_stock = 0  

    # 마지막 주식이 남아있을 경우 매도
    if s_stock:
        s_money += s_stock * stocks[-1]

    return s_money


def compare_stocks(bnp_money, timing_money):
    if bnp_money > timing_money:
        return 'BNP'
    elif bnp_money < timing_money:
        return 'TIMING'
    else:
        return 'SAMESAME'


# test_arr = [10, 20, 23, 34, 55, 30, 22, 19, 12, 45, 23, 44, 34, 38]
# test_arr2 = [20, 20, 33, 98, 15, 6, 4, 1, 1, 1, 2, 3, 6, 14]

# print(bnp_investment(test_arr, 100)) # 380

# print(bnp_investment(test_arr2, 15)) #14

# print(timing_investment(test_arr, 100)) # 195

# print(timing_investment(test_arr2, 15)) # 36


print(compare_stocks(bnp_investment(stock_arr, buying_power), timing_investment(stock_arr, buying_power)))