def solution(s):
    s = s.lower()
    p_cnt, y_cnt = 0, 0
    for ch in s:
        if ch == 'p':
            p_cnt += 1
        elif ch == 'y':
            y_cnt += 1
    if p_cnt == y_cnt:
        return True
    return False

# Other Solution 1.
# from collections import Counter
# def solution(s):
#     c = Counter(s.lower())
#     return c['p'] == c['y']

# Other Solution 2.
# def solution(s):
#     return s.lower().count('p') == s.lower().count('y')