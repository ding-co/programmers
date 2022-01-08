def solution(left, right):
    def countDivisors(num):
        cnt = 0
        for i in range(1, (num // 2) + 1):
            if num % i == 0:
                cnt += 1
        return cnt + 1
    
    result = 0
    for num in range(left, right + 1):
        if countDivisors(num) % 2 == 0:
            result += num
        else:
            result -= num
    
    return result

# Other Solution 1.
# 제곱수는 약수의 개수가 홀수개
# def solution(left, right):
#     answer = 0
#     for num in range(left, right + 1):
#         if int(num ** 0.5) == num ** 0.5:
#             answer -= num
#         else:
#             answer += num
#     return answer

# Other Solution 2.
