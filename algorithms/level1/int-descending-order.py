def solution(n):
    n_list = sorted(list(str(n)), reverse=True)
    return int(''.join(n_list))