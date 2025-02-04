""" 
문제) 왕비를 피해 일곱 난쟁이들과 함께 평화롭게 생활하고 있던 백설공주에게 위기가 찾아왔다. 일과를 마치고 돌아온 난쟁이가 일곱 명이 아닌 아홉 명이었던 것이다.

아홉 명의 난쟁이는 모두 자신이 "백설 공주와 일곱 난쟁이"의 주인공이라고 주장했다. 뛰어난 수학적 직관력을 가지고 있던 백설공주는, 다행스럽게도 일곱 난쟁이의 키의 합이 100이 됨을 기억해 냈다.

아홉 난쟁이의 키가 주어졌을 때, 백설공주를 도와 일곱 난쟁이를 찾는 프로그램을 작성하시오. 
"""

# input = 20 7 23 19 10 15 25 8 13
# output = 7 8 10 13 19 20 23

# input 총 합을 계산
# input - arr[i] - arr[j] = 100 을 찾아서, 9명에서 2명을 뺌으로써 7명을 구함
# 제외할 2명을 찾고 나머지 7명을 추가해 오름차순으로 정리한 후에 리턴한다.
 
# 첫번째 시도 브루트포스
def find_seven_people(arr):
    total_sum = sum(arr)

    remove_arr = []

    res = []

    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if total_sum - arr[i] - arr[j] == 100:
                remove_arr.append(arr[i])
                remove_arr.append(arr[j])
                break

    res = [arr[i] for i in range(len(arr)) if arr[i] not in remove_arr]

    res.sort()

    return res

test_input = [20, 7, 23, 19, 10, 15, 25, 8, 13]

print(find_seven_people(test_input))


# # 백준 제출 답안
# # 백준 input은 배열이지 않고 라인마다 자연수가 나뉘어서 주어진다 
# # output 또한 각 라인마다 자연수가 출력된다
# """ 
# input
# 20
# 7
# 23
# 19
# 10
# 15
# 25
# 8
# 13

# output 
# 7
# 8
# 10
# 13
# 19
# 20
# 23
# """ 

def find_seven_people_baekjoon():
    import sys

    input = sys.stdin.readline

    arr = []

    for _ in range(9):
        arr.append(int(input()))
        
    total_sum = sum(arr)
    remove_arr = []

    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if total_sum - arr[i] - arr[j] == 100:
                remove_arr.append(arr[i])
                remove_arr.append(arr[j])
                break
        
        
    arr.remove(remove_arr[0])
    arr.remove(remove_arr[1])

    arr.sort()

    for i in arr:
        print(i)
