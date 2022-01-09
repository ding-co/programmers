def solution(nums):
    max_result = len(nums) // 2
    set_nums = len(set(nums))
    if max_result <= set_nums:
        return max_result
    return set_nums

# Other Solution
# def solution(nums):
#     return min(len(nums)/2, len(set(nums)))