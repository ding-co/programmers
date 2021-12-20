def solution(arr):
    answer = []
    if len(arr) == 1:
        answer.append(-1)
    else:
        smallest_number = min(arr)
        arr.remove(smallest_number)
        answer = arr
    return answer