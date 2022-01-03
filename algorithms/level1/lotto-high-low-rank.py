def solution(lottos, win_nums):
    lotto_check_list = [0] * 45
    count_list = [0, 0]
    
    for num in win_nums:
        lotto_check_list[num - 1] += 1
    
    for num in lottos:
        if num == 0:
            count_list[0] += 1
        elif lotto_check_list[num - 1] == 1:
            count_list[0] += 1
            count_list[1] += 1
    
    for i in range(len(count_list)):
        if count_list[i] == 0:
            count_list[i] = 6
        else:
            count_list[i] = 6 - count_list[i] + 1
    
    return count_list

# Other Solution 1.

# def solution(lottos, win_nums):
#     rank = [6, 6, 5, 4, 3, 2, 1]
    
#     cnt_0 = lottos.count(0)
#     ans = 0
    
#     for num in lottos:
#         if num in win_nums:
#             ans += 1
    
#     return [rank[ans + cnt_0], rank[ans]]

# Other Solution 2.

# def solution(lottos, win_nums):
#     rank = {
#         0: 6,
#         1: 6,
#         2: 5,
#         3: 4,
#         4: 3,
#         5: 2,
#         6: 1
#     }
    
#     return [ \
#         rank[len( (set(lottos) & set(win_nums))) + lottos.count(0)], \
#         rank[len( (set(lottos) & set(win_nums)) )] \
#     ]