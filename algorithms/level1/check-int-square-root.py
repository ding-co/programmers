import math
def solution(n):
    answer = 0
    square_root = math.sqrt(n)
    square_root_items = str(square_root).split('.')
    if square_root_items[1] == '0':
        answer = (int(square_root) + 1) ** 2
    else:
        answer = -1
    return answer

# Other Solution
# def solution(n):
#     square_root = n ** (1/2)
#     if (square_root % 1 == 0):
#         return (square_root + 1) ** 2
#     return -1