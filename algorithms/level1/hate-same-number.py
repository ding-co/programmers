# Other Solution
def solution(arr):
    answer = []
    save_num = -1
    for item in arr:
        if save_num != item:
            save_num = item
            answer.append(item)
    return answer