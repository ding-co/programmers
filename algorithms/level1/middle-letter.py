def solution(s):
    answer = ''
    mid_s = len(s) // 2
    if len(s) % 2 == 1:
        answer += s[mid_s]
    else:
        answer += s[mid_s - 1 : mid_s + 1]
    return answer