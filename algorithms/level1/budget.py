def solution(d, budget):
    d.sort()
    result = 0
    sum = 0
    for element in d:
        sum += element
        result += 1
        if sum > budget:
            sum -= element
            result -= 1
            break
    return result

# Other Solution 1
# def solution(d, budget):
#     d.sort()
#     while budget < sum(d):
#         d.pop()
#     return len(d)

# Other Solution 2
# def solution(d, budget):
#     d.sort()
#     cnt = 0
#     for element in d:
#         budget -= element
#         if budget < 0:
#             break
#         cnt += 1
#     return cnt