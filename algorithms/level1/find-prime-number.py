def solution(n):
    def is_prime(num):
        arr = [True] * (num + 1)
        for i in range(2, num + 1):
            if arr[i] == True:
                j = 2
                while (i * j) <= n:
                    arr[i * j] = False
                    j += 1
        return arr
    
    cnt = 0
    is_prime_list = is_prime(n)
    for i in range(2, len(is_prime_list)):
        if is_prime_list[i] == True:
            cnt += 1
    return cnt

# Other Solution
# def solution(n):
#     num = set(range(2, n + 1))
#     for i in range(2, n + 1):
#         if i in num:
#             num -= set(range(2 * i, n + 1, i))
#     return len(num)