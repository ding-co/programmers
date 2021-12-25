def solution(a, b):
    answer = 0
    left, right = min(a, b), max(a, b)
    for num in range(left, right + 1):
        answer += num
    return answer