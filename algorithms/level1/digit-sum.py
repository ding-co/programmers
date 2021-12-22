def solution(n):
    answer = 0

    for ch in str(n):
        answer += int(ch)

    return answer

# Other Solution
# def solution(n):
#     answer = 0

#     if n < 10:
#         return n
#     else:
#         return (n % 10) + solution(n // 10)

#     return answer