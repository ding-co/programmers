def solution(n):
    answer = ''
    for i in range(n):
        if i % 2 == 0:
            answer += '수'
        else:
            answer += '박'
    return answer

# Other Solution
# def solution(n):
#     return "".join(["수박"[i%2] for i in range(n)])