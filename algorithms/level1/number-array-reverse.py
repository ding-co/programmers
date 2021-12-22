def solution(n):
    answer = list(map(int, str(n)))
    answer.reverse()
    return answer

# Other Solution
# def solution(n):
#     answer = list(map(int, reversed(str(n))))
#     return answer