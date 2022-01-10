from collections import Counter
def solution(participant, completion):
    cnt_dict = Counter(participant)
    for i in completion:
        if i in cnt_dict:
            cnt_dict[i] -= 1
    return cnt_dict.most_common(1)[0][0]

# Other Solution
# from collections import Counter
# def solution(participant, completion):
#     result_cnt = Counter(participant) - Counter(completion)
#     return list(result_cnt.keys())[0]