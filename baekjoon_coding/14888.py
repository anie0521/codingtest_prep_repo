import sys

N = int(sys.stdin.readline())

nums = list(map(int, sys.stdin.readline().split()))

# + - * //
add, sub, mul, div = map(int, input().split())

max_res = -float('inf')
min_res = float('inf')


def backtracking(idx, cur_num, add, sub, mul, div):
    global max_res, min_res
    if idx == N - 1:
        max_res = max(max_res, cur_num)
        min_res = min(min_res, cur_num)

    if add > 0:
        backtracking(idx + 1, cur_num + nums[idx + 1], add - 1, sub, mul, div)
    
    if sub > 0:
        backtracking(idx + 1, cur_num - nums[idx + 1], add, sub - 1, mul, div)

    if mul > 0:
        backtracking(idx + 1, cur_num * nums[idx + 1], add, sub, mul - 1, div)
    
    if div > 0:
        if cur_num < 0:
            backtracking(idx + 1, -(-cur_num // nums[idx + 1]), add, sub, mul, div - 1)
        else:
            backtracking(idx + 1, cur_num // nums[idx + 1], add, sub, mul, div - 1)


backtracking(0, nums[0], add, sub, mul, div)

print(max_res)
print(min_res)