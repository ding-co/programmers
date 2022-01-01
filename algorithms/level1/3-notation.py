def solution(n):
    n_3 = ""
    while n > 0:
        n, mod = divmod(n, 3)
        n_3 += str(mod)
    return int(n_3, 3)

# Other Solution
# def solution(n):
#     n_3 = ""
#     while n:
#         n_3 += str(n % 3)
#         n //= 3
#     return int(n_3, 3)